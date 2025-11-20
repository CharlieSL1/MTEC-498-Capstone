# Week 11 Progression

## What changed
- Top-camera depth tracking (OAK-D) cleaned up and streaming `/xyz` OSC into Max/Ableton with the current device state.
- Gesture → OSC sender now throttles and is env-configurable (`OSC_IP`, `OSC_PORT`, `OSC_GESTURE_PORT`) to address over-sensitive Max input.
- MediaPipe gesture model path resolves relative to this snapshot so it loads cleanly inside `Project/Week11`.
- Imported the latest Max for Live device `PanGu.amxd` from the Ableton preset path for this week’s drop.

## Files in this drop
- `main.py` — starts depth sender thread, emits gesture + XYZ over OSC.
- `Vision_Module/depthcameraToMax.py` — DepthAI pipeline pushing `/xyz`, `/xyz/x`, `/xyz/y`, `/xyz/z`.
- `Vision_Module/mediapipe_dataSet.py` — Live gesture recognizer using `gesture_recognizer.task` in this folder.
- `Vision_Module/dataToMax.py` — Gesture → OSC with a 10ms throttle and configurable ports.
- `Vision_Module/gesture_recognizer.task` — MediaPipe gesture model.
- `Max_Audio_Effect/PanGu.amxd` — Max for Live device (imported from `Perform Project/Presets/Audio Effects/Max Audio Effect`).

## How to run
1) `cd Project/Week11`
2) Install deps: `pip install depthai mediapipe python-osc opencv-python`
3) (Optional) Set OSC targets:  
   - Depth stream: `export OSC_IP=127.0.0.1 OSC_PORT=9000` (defaults)  
   - Gesture stream: `export OSC_GESTURE_PORT=7400` (falls back to `OSC_PORT` if set)
4) Run: `python main.py`
5) Open `Max_Audio_Effect/PanGu.amxd` inside your Ableton set to receive gestures/XYZ.

## Next steps
- Tune Max smoothing to balance responsiveness vs. stability for both gesture and depth streams.
- Add CLI flags for camera index + OSC targets to avoid env dependencies.
- Add lightweight logging of OSC send rates to monitor remaining spikes.
