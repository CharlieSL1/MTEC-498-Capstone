import os
import time
from pythonosc.udp_client import SimpleUDPClient

OSC_IP = os.getenv("OSC_IP", "127.0.0.1")
# Allow overriding the gesture port separately; fall back to OSC_PORT or 7400
OSC_PORT = int(os.getenv("OSC_GESTURE_PORT", os.getenv("OSC_PORT", "7400")))

client = SimpleUDPClient(OSC_IP, OSC_PORT)

def send_gesture(gesture_name):
    # Map gesture names to numbers
    gesture_map = {
        "Open_Palm": 1,
        "Closed_Fist": 2,
        "Pointing_Up": 3,
        "Victory": 4,
        "Thumb_Up": 5,
        "Thumb_Down": 6
    }
    
    # Get gesture number
    gesture_number = gesture_map.get(gesture_name, 0)
    
    # Send OSC message
    client.send_message("/gesture", gesture_number)
    time.sleep(0.01)
    print(f"Sent gesture '{gesture_name}' as number: {gesture_number} -> {OSC_IP}:{OSC_PORT}")


if __name__ == "__main__":
    # Test sending different gestures
    send_gesture("Open_Palm")
    send_gesture("Closed_Fist")
    send_gesture("Pointing_Up")
