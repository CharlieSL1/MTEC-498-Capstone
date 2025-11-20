import depthai as dai
import numpy as np
import time
import sys
import threading
from pythonosc.udp_client import SimpleUDPClient


# OSC client setup for sending XYZ data to Max/MSP
import os

OSC_IP = os.getenv("OSC_IP", "127.0.0.1")
# Use a common alternative UDP port; can override via OSC_PORT env
OSC_PORT = int(os.getenv("OSC_PORT", "9000"))
OSC_VERBOSE = os.getenv("OSC_VERBOSE", "0") == "1"
osc_client = SimpleUDPClient(OSC_IP, OSC_PORT)

# Shared variable to store latest XYZ values
latest_xyz = {"x": 0, "y": 0, "z": 0}
xyz_lock = threading.Lock()


def send_xyz_to_max(x, y, z, pixel_x=None, pixel_y=None):
    """
    Send XYZ coordinates to Max/MSP via OSC.
    Sends x, y, z as integers to port 7401. Also sends individual axis paths.
    
    Args:
        x: X coordinate in mm
        y: Y coordinate in mm  
        z: Z coordinate (depth) in mm
        pixel_x: Optional pixel X coordinate (not sent)
        pixel_y: Optional pixel Y coordinate (not sent)
    """
    # Convert mm -> cm and round to integers
    xi, yi, zi = int(round(x / 10.0)), int(round(y / 10.0)), int(round(z / 10.0))

    # Update shared variable with latest XYZ values
    global latest_xyz
    with xyz_lock:
        latest_xyz = {"x": xi, "y": yi, "z": zi}

    # Send XYZ coordinates as a list of three integers [X, Y, Z]
    osc_client.send_message("/xyz", [xi, yi, zi])

    # Optional verbose logging for debugging OSC visibility in Max
    if OSC_VERBOSE:
        print(f"[OSC->{OSC_IP}:{OSC_PORT}] /xyz {xi} {yi} {zi}")


def print_result():
    """
    Get and print the latest XYZ coordinates.
    Similar to gesture_recognizer.print_result()
    
    Returns:
        tuple: (x, y, z) coordinates as integers, or (None, None, None) if no data
    """
    global latest_xyz
    with xyz_lock:
        x, y, z = latest_xyz["x"], latest_xyz["y"], latest_xyz["z"]
    
    if x == 0 and y == 0 and z == 0:
        return None, None, None
    
    print(f"XYZ: X={x}mm, Y={y}mm, Z={z}mm")
    return x, y, z


def check_device_permissions():
    """Check if devices are available and provide helpful error messages."""
    try:
        # Try to get available devices (method may vary by DepthAI version)
        devices = dai.Device.getAllAvailableDevices()
        if len(devices) == 0:
            print("Warning: Device detection returned no devices.")
            print("This might be a detection issue. Will attempt to connect anyway...")
            print("\nTroubleshooting steps:")
            print("1. Make sure your OAK camera is connected via USB")
            print("2. Check if the device appears in System Information > USB")
            print("3. Try unplugging and reconnecting the camera")
            print("4. If using OAK Viewer, make sure it's not blocking the connection")
            return True  # Continue anyway, let connection attempt show the real error
        
        print(f"Found {len(devices)} device(s):")
        for device in devices:
            print(f"  - {device.name} ({device.state})")
        return True
    except AttributeError:
        # getAllAvailableDevices might not exist in this version
        print("Note: Device enumeration not available in this DepthAI version.")
        print("Will attempt direct connection...")
        return True
    except Exception as e:
        if "X_LINK_INSUFFICIENT_PERMISSIONS" in str(e) or "INSUFFICIENT_PERMISSIONS" in str(e):
            print("=" * 60)
            print("ERROR: Insufficient permissions to access DepthAI device")
            print("=" * 60)
            print("\nOn macOS, you may need to:")
            print("1. Grant USB permissions in System Settings > Privacy & Security")
            print("2. Or run with sudo (temporary solution):")
            print("   sudo python depthcameraToMax")
            print("\nFor more information, see:")
            print("https://docs.luxonis.com/projects/api/en/latest/installation/#usb-permissions")
            print("=" * 60)
            return False
        else:
            print(f"Note: Device detection error: {e}")
            print("Will attempt direct connection anyway...")
            return True  # Continue, let the actual connection show the real error


def main():
    """
    Fetch XYZ (mm) from the OAK-D Pro W PoE using DepthAI v3.
    Uses Camera nodes (configured as MONO), StereoDepth depth output, and host-side
    intrinsics to derive XYZ coordinates.
    Reference: https://docs.luxonis.com/software-v3/depthai/
    """
    # Check device availability and permissions first
    if not check_device_permissions():
        sys.exit(1)
    
    # Create pipeline
    try:
        pipeline = dai.Pipeline()
    except Exception as e:
        if "X_LINK_INSUFFICIENT_PERMISSIONS" in str(e) or "INSUFFICIENT_PERMISSIONS" in str(e):
            print("\nPermission error during pipeline creation.")
            print("Try running with sudo or check USB permissions.")
            sys.exit(1)
        raise

    # Create left/right mono cameras (using unified Camera node in DepthAI v3)
    # Build with the board socket to select which sensor to use
    monoLeft = pipeline.create(dai.node.Camera).build(dai.CameraBoardSocket.CAM_B)
    monoRight = pipeline.create(dai.node.Camera).build(dai.CameraBoardSocket.CAM_C)
    
    # Set camera properties - using the correct v3 API
    # Reference: https://docs.luxonis.com/software-v3/depthai/
    monoLeft.setSensorType(dai.CameraSensorType.MONO)
    monoRight.setSensorType(dai.CameraSensorType.MONO)

    # Request outputs at a known resolution to avoid stride mismatches
    # (StereoDepth expects left/right frames with matching width/stride)
    stereo_w, stereo_h = 1280, 720
    left_out = monoLeft.requestOutput(size=(stereo_w, stereo_h), type=dai.ImgFrame.Type.RAW8)
    right_out = monoRight.requestOutput(size=(stereo_w, stereo_h), type=dai.ImgFrame.Type.RAW8)

    # Create stereo depth node
    stereo = pipeline.create(dai.node.StereoDepth)
    stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.FAST_DENSITY)
    stereo.setInputResolution(stereo_w, stereo_h)
    
    # Link cameras to stereo depth (Camera nodes use .raw for raw sensor output)
    left_out.link(stereo.left)
    right_out.link(stereo.right)

    # Host-facing depth queue directly from output (v3 removes XLinkOut)
    depth_queue = stereo.depth.createOutputQueue(maxSize=4, blocking=False)

    # Connect to device and start pipeline
    try:
        print("\nConnecting to device...")
        print("If you see 'No DepthAI devices found', try:")
        print("  - Closing OAK Viewer if it's open (it may be using the device)")
        print("  - Unplugging and reconnecting the camera")
        print("  - Checking USB permissions in System Settings\n")
        
        pipeline.start()
        device = pipeline.getDefaultDevice()
        calib = device.readCalibration()

        print("Depth camera initialized. Press Ctrl+C to exit.")
        print(f"Sending XYZ data to Max/MSP via OSC at {OSC_IP}:{OSC_PORT}")
        print("OSC messages:")
        print("  /xyz [X, Y, Z] - Three integers (x, y, z in mm)")
        print("  /xyz/x, /xyz/y, /xyz/z - Individual integer axes\n")
        if OSC_VERBOSE:
            print("OSC_VERBOSE=1 so each send will be logged to console.\n")
        
        frame_count = 0
        while pipeline.isRunning():
            # Check if queue has data before getting
            if depth_queue.has():
                depth_msg = depth_queue.get()
                depth_frame = depth_msg.getFrame()  # depth in millimeters
                h, w = depth_frame.shape
                frame_count += 1

                # Try center pixel first, then try nearby pixels if center is invalid
                x, y = w // 2, h // 2
                z = depth_frame[y, x].item()
                
                # If center pixel is invalid, try a small region around it
                if z == 0 or np.isnan(z):
                    # Try a 5x5 region around center
                    search_radius = 2
                    valid_z = None
                    for dy in range(-search_radius, search_radius + 1):
                        for dx in range(-search_radius, search_radius + 1):
                            try_y = y + dy
                            try_x = x + dx
                            if 0 <= try_y < h and 0 <= try_x < w:
                                try_z = depth_frame[try_y, try_x].item()
                                if try_z > 0 and not np.isnan(try_z):
                                    valid_z = try_z
                                    x, y = try_x, try_y
                                    z = valid_z
                                    break
                        if valid_z is not None:
                            break
                
                # Debug: Print depth info every 30 frames
                if frame_count % 30 == 0:
                    # Calculate depth statistics
                    valid_depths = depth_frame[(depth_frame > 0) & ~np.isnan(depth_frame)]
                    if len(valid_depths) > 0:
                        min_depth = np.min(valid_depths)
                        max_depth = np.max(valid_depths)
                        mean_depth = np.mean(valid_depths)
                        print(f"Frame {frame_count}: Depth stats - Min: {min_depth:.1f}mm, Max: {max_depth:.1f}mm, Mean: {mean_depth:.1f}mm")
                        print(f"  Valid depth pixels: {len(valid_depths)}/{w*h} ({100*len(valid_depths)/(w*h):.1f}%)")
                    print(f"  Using pixel ({x},{y}), depth = {z}mm")

                # Skip if depth is still invalid after search
                if z == 0 or np.isnan(z):
                    if frame_count % 30 == 0:
                        print(f"  Warning: No valid depth found, skipping frame...")
                    continue

                # Compute XYZ using intrinsics for CAM_B at current resolution
                try:
                    intrinsics = np.array(calib.getCameraIntrinsics(dai.CameraBoardSocket.CAM_B, w, h))
                    fx, fy = intrinsics[0, 0], intrinsics[1, 1]
                    cx, cy = intrinsics[0, 2], intrinsics[1, 2]

                    # Check for division by zero
                    if fx == 0 or fy == 0:
                        print(f"Warning: Invalid camera intrinsics (fx={fx}, fy={fy})")
                        continue

                    # Convert pixel coordinates to 3D coordinates
                    X = (x - cx) * z / fx
                    Y = (y - cy) * z / fy
                    xyz_int = np.array([X, Y, z], dtype=np.int32)
                    
                    # Print to console (values shown in cm)
                    print(f"XYZ at pixel ({x},{y}): X={X/10:.2f}cm, Y={Y/10:.2f}cm, Z={z/10:.2f}cm")
                    
                    # Send XYZ coordinates to Max/MSP via OSC
                    try:
                        send_xyz_to_max(X, Y, z, pixel_x=x, pixel_y=y)
                    except Exception as osc_error:
                        print(f"OSC send error: {osc_error}")
                    
                except Exception as e:
                    print(f"Error computing XYZ: {e}")
                    import traceback
                    traceback.print_exc()
                    continue
            else:
                time.sleep(0.01)  # Small delay to avoid busy-waiting
                
    except KeyboardInterrupt:
        print("\nExiting...")
    except RuntimeError as e:
        error_str = str(e)
        if "X_LINK_INSUFFICIENT_PERMISSIONS" in error_str or "INSUFFICIENT_PERMISSIONS" in error_str:
            print("\n" + "=" * 60)
            print("ERROR: Insufficient permissions to access DepthAI device")
            print("=" * 60)
            print("\nOn macOS, try one of the following:")
            print("1. Grant USB permissions in System Settings > Privacy & Security > USB")
            print("2. Run with sudo (temporary solution):")
            print("   sudo python depthcameraToMax")
            print("\nFor detailed setup instructions, see:")
            print("https://docs.luxonis.com/projects/api/en/latest/installation/#usb-permissions")
            print("=" * 60)
            sys.exit(1)
        else:
            print(f"\nRuntime error: {e}")
            raise
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        raise
    finally:
        try:
            pipeline.stop()
        except Exception:
            pass


if __name__ == "__main__":
    main()
