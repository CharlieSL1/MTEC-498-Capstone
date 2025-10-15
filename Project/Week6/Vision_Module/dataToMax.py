from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 7400

client = SimpleUDPClient(ip, port)

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
    print(f"Sent gesture '{gesture_name}' as number: {gesture_number}")


if __name__ == "__main__":
    # Test sending different gestures
    send_gesture("Open_Palm")
    send_gesture("Closed_Fist")
    send_gesture("Pointing_Up")