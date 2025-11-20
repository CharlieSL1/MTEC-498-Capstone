'''
This module is used to create a gesture recognizer instance with the live stream mode.
Data will return the vaule of the gesture recognition result to Max/Msp to control different functions.

To do List:
1. Use OpenCV to capture the video stream from the webcam [X]
2. Use the gesture recognizer to recognize the gesture in the video stream [X]
3. Return the gesture recognition result to main.py[X]
'''


import cv2 as cv
from pathlib import Path
import mediapipe as mp
import time

# Resolve the task file relative to this module so it works in the week folder snapshot
MODEL_PATH = Path(__file__).resolve().parent / "gesture_recognizer.task"

# Default to built-in camera; swap index if using an external webcam
BuildinCamera = cv.VideoCapture(0)
if not BuildinCamera.isOpened():
    print("Error: Could not open BuildinCamera")
    exit()

# Gesture Recognizer setup
BaseOptions = mp.tasks.BaseOptions
base_options = BaseOptions(model_asset_path=str(MODEL_PATH))
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Gesture Recognizer Callback Function
from . import dataToMax as Max_data

def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    if result.gestures:
        gesture = result.gestures[0][0].category_name
        confidence = result.gestures[0][0].score
        Max_data.send_gesture(gesture)
        return print(f"Gesture: {gesture}, Confidence: {confidence:.2f}")
    else:
        return None, None


# Create a gesture recognizer instance with the live stream mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=str(MODEL_PATH)),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

with GestureRecognizer.create_from_options(options) as recognizer:
    # BuildInCamera Activate
    while True:
        ret, frame = BuildinCamera.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Convert frame to MediaPipe image and recognize gesture
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        frame_timestamp_ms = int(time.time() * 1000)
        recognizer.recognize_async(mp_image, frame_timestamp_ms)
        if cv.waitKey(1) == ord('q'):
            break
