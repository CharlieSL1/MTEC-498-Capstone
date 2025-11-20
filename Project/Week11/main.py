import threading
import time

import Vision_Module.mediapipe_dataSet as gesture_recognizer
import Vision_Module.dataToMax as Max_data
import Vision_Module.depthcameraToMax as depthcamera_data


def main():
    # Start depth/XYZ sender in a background thread
    depth_thread = threading.Thread(target=depthcamera_data.main, daemon=True)
    depth_thread.start()

    # Give the depth pipeline a moment to start
    time.sleep(2)

    # Send the current gesture via OSC
    Max_data.send_gesture(gesture_recognizer.print_result())

    # Fetch and print the latest XYZ values
    x, y, z = depthcamera_data.print_result()
    if x is not None:
        print(f"Current XYZ coordinates: X={x}mm, Y={y}mm, Z={z}mm")

    # Keep the process alive while the depth thread runs
    try:
        while depth_thread.is_alive():
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
