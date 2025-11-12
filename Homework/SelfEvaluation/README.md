# MTEC-498 Self-Evaluation Presentation

## Overview
This folder contains materials for the MTEC-498 Self-Evaluation Presentation, representing a comprehensive assessment of my performance, growth, and achievements throughout the capstone course.

## Contents
- `README.md` - This documentation file
- `MTEC-498-Capstone-Filled-by-Repo.pdf` - Self-evaluation presentation slides
- `Comprehensive_Self_Evaluation.md` - Complete 8-minute presentation content
- `SupportingMaterials/` - Supporting evidence and documentation
  - `Achievement_Analysis.md` - Detailed technical accomplishments
  - `Code_Analysis.md` - Code analysis and technical evidence
  - `Evidence_Documentation.md` - Supporting evidence for all claims
  - `PanGu.amxd` - Max for Live spatial audio device used in the live demo

## Project Summary
**PanGu — Spatial Audio, Live Phase Controller & Composition Assistant**

A next-generation spatial audio performance platform featuring a wearable, arm-mounted Circle MIDI controller that enables musicians to select positions in 3D space and instantly play/place sounds there—transforming spatial audio into an expressive instrument for composition and live performance.

## Key Achievements
- Developed gesture recognition system using MediaPipe
- Implemented OSC communication between Python and Max/MSP
- Created modular system architecture for spatial audio control
- Integrated computer vision with real-time audio processing
- Built comprehensive documentation and project structure

## Technical Skills Demonstrated
- Python programming (MediaPipe, OpenCV, OSC)
- Max/MSP integration and audio processing
- Computer vision and gesture recognition
- System architecture and modular design
- Documentation and project management

## Learning Outcomes Assessment
This self-evaluation will assess achievement across all course learning outcomes with specific evidence from the PanGu project development.

## Latest Update — Week 10
- Matched the MediaPipe depth-camera vision module with Ableton Live through the custom `PanGu.amxd` Max for Live audio effect, closing the loop from gesture capture to DAW control.
- Verified end-to-end OSC routing (vision module `dataToMax.py` → `PanGu.amxd`) so each of the six trained gestures reliably toggles spatial routing, looping, and macro parameters inside Live.
- Documented the pipeline inside the Self-Evaluation presentation materials and exported the Max device into `SupportingMaterials/` for grading-ready evidence.
- Next milestone: rehearse a full performance that layers gesture-triggered spatial loops with depth-camera tracking inside Ableton Live’s Session View.
