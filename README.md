# MTEC-498-Capstone
# PanGu — Spatial Audio, Live Phase Controller & Composition Assistant
- [PanGu_V1](PanGu_V1.jpg)
- [PanGu_Flow_Chart](PanGu.png)
- [PanGu_ppt](PanGu.pdf)

> **Elevator Pitch**  
> A next-generation **spatial audio performance platform**: a wearable, arm-mounted **Circle MIDI controller** that lets you **select a position in 3D space** and then **instantly play/place sounds there**—turning spatial audio into an expressive **instrument** for composition and live performance.

---

## Table of Contents
- [Project Overview](#project-overview)
  - [Problem Statement](#problem-statement)
  - [Creative Vision](#creative-vision)
  - [Significance](#significance)
  - [Personal Connection](#personal-connection)
- [Users & Needs](#users--needs)
  - [Primary Users](#primary-users)
  - [Use Cases](#use-cases)
  - [User Needs](#user-needs)
- [Why Me](#why-me)
- [Technical Specifications](#technical-specifications)
- [Influences & Inspirations](#influences--inspirations)
- [Project Timeline](#project-timeline)
- [Risk & Mitigation](#risk--mitigation)
- [Next Steps](#next-steps)
- [Beyond This Semester](#beyond-this-semester)
- [Contact](#contact)
- [Credits](#credits)

---

## Project Overview

### Problem Statement
Current music creation/performance tools for spatial audio are either **too technical** (post-production/DAW-bound) or **too experimental** (unreliable gestures, weak integration). Musicians lack an **intuitive, real-time** way to treat sound as a **tangible object** that can be positioned and **performed** in space.

### Creative Vision
Build a platform that makes sound feel **grabbable**. Combine a **pan controller** with a **wearable hexagonal MIDI interface** so musicians can first **select 3D positions** and then **perform** them—transforming spatial audio from an engineering task into a **new instrument**.

### Significance
Spatial audio is expanding across **gaming, VR/AR, film, and live music**. Tools lag in **accessibility** and **playability**. This project bridges **cutting-edge spatialization** with **embodied performance**, offering an **intuitive, expressive** path into immersive sound.

### Personal Connection
As a **composer–technologist**, I feel the gap between **imagined spatial sound** and **cumbersome tooling**. This project aims to **collapse that gap**—making spatial design as immediate as **strumming a chord** or **hitting a drum**.

---

## Users & Needs

### Primary Users
Musicians, producers, sound artists, and audiences exploring **new performance formats**.

### Use Cases
- **Studio**: Rapidly test spatial effects during composition/production.  
- **Live Performance**: Use as an **expressive instrument** for immersive shows.  
- **Art Exhibitions**: Let audiences **intuitively interact** with spatial audio.

### User Needs
**Intuitive control**, **real-time feedback**, and **low learning barriers**—turning spatial audio from complex tooling into an **accessible performance medium**.

---

## Why Me
- **Relevant Coursework**: EDI prototyping; Programming in C; Programming in Max  
- **Previous Projects**: *Box of World*; *Ultra Sonic Headphone*  
- **Personal Interests**: Multichannel composer; music-tech developer  
- **Technical Strengths**: Python, C/C++, Max/MSP, circuit design  
- **Learning Goals**: Deepen **spatial audio** skills

---

## Technical Specifications
**Programming Languages**: Python, C/C++, Max  
**Frameworks/Libraries**: Max/MSP; Arduino ecosystem  
**Audio Technologies**: TorchAudio; DSP  
**AI/ML**: PyTorch; scikit-learn; NumPy

---

## Influences & Inspirations
- **Lumatone** *(Product)* — rethinking playing/performing systems  
- **MiMU Gloves** *(Product)* — making creation **fun** and **immersive**  
- **PanMan** *(NIME Paper)* — approaches to **panning** and **modularizing** spatial components

---

## Project Timeline

| Phase | Weeks | Focus |
|---|---|---|
| **Phase 1** | 1–3 | Component checks; sensor bring-up; circuit design |
| **Phase 2** | 4–7 | 3D modeling & printing; tech development |
| **Phase 3** | 8–10 | OS/UX design; continued tech development |
| **Phase 4** | 11–13 | Iteration & improvements |
| **Phase 5** | 14–15 | Paper writing; function checks; mini-performance (NIME) |

---

## Recent Progress Updates

### Week 8-9: PanGuStudio Swift Application Development

This week and the previous week have focused on building the core **PanGuStudio** application in Swift, creating a cross-platform (iOS/macOS) spatial audio control system.

#### Key Achievements

**1. Project Architecture & Setup**
- Established the complete PanGuStudio Xcode project structure
- Implemented modular architecture with separate modules for:
  - **DSP**: Audio processing and spatialization (`AudioEngine.swift`, `Spatializer.swift`)
  - **Camera**: Hand pose detection and gesture recognition (`HandPoseService.swift`, `HandGestureClassifier.swift`)
  - **IO**: MIDI and OSC communication (`MIDIClient.swift`, `OSCClient.swift`)
  - **UI**: SwiftUI interface components and views
  - **Utils**: Diagnostics, smoothing, and settings management

**2. Package Dependencies & Integration**
- Integrated **AudioKit** ecosystem:
  - `AudioKit` (v5.6.0+)
  - `AudioKitEX` (v5.6.2+) - Extended audio components
  - `SoundpipeAudioKit` (v5.7.3+) - Soundpipe DSP algorithms
- Resolved package dependency linking issues
- Configured proper package product dependencies in Xcode project

**3. Multi-Platform Support**
- Implemented conditional compilation for iOS/macOS compatibility:
  - `CameraPreviewView.swift`: Uses `UIViewRepresentable` on iOS, `NSViewRepresentable` on macOS
  - `SettingsView.swift`: Platform-specific pasteboard handling (UIKit/AppKit)
- Ensured all UI components work across both platforms

**4. Core Functionality Implementation**

**Audio Engine** (`PanGuStudio/PanGuStudio/DSP/AudioEngine.swift`):
- Dynamic oscillator with preset management
- Costello reverb integration
- Real-time audio looping/recording
- Spatial audio engine integration
- Latency monitoring and diagnostics

**Hand Pose Service** (`PanGuStudio/PanGuStudio/Camera/HandPoseService.swift`):
- Vision framework integration for hand tracking
- Real-time gesture classification
- FPS estimation and performance monitoring
- Async/await actor-based architecture for thread safety

**MIDI Client** (`PanGuStudio/PanGuStudio/IO/MIDIClient.swift`):
- CoreMIDI integration with virtual source support
- Continuous control (CC) message sending
- Program change and real-time message support
- Network MIDI session support
- Hardware destination detection

**App State Management** (`PanGuStudio/PanGuStudio/AppState/AppState.swift`):
- Centralized state management using Combine
- Reactive gesture-to-audio mapping
- Settings persistence
- Real-time diagnostics aggregation

**5. Technical Challenges Resolved**
- Fixed Swift actor isolation issues in async delegate methods
- Resolved type conversion errors (Int → UInt8 for MIDI)
- Fixed CoreMIDI API compatibility issues
- Implemented proper error handling for audio engine initialization
- Added comprehensive diagnostics and monitoring

**6. Gesture Recognition Pipeline**
- **Vision Module** (`Vision_Module/mediapipe_dataSet.py`): Python-based MediaPipe gesture recognition
- **Hand Gesture Classifier** (`HandGestureClassifier.swift`): Swift-based gesture classification from hand landmarks
- Support for 6 gesture types: Open Palm, Closed Fist, Pointing Up, Victory, Thumb Up, Thumb Down
- Real-time confidence scoring and smoothing

#### Key Files Reference

**Core Application Files:**
- [`PanGuStudio/PanGuStudio/PanGuStudioApp.swift`](../PANGU/PanGuStudio/PanGuStudio/PanGuStudioApp.swift) - Main application entry point
- [`PanGuStudio/PanGuStudio/AppState/AppState.swift`](../PANGU/PanGuStudio/PanGuStudio/AppState/AppState.swift) - Centralized state management
- [`PanGuStudio/PanGuStudio/DSP/AudioEngine.swift`](../PANGU/PanGuStudio/PanGuStudio/DSP/AudioEngine.swift) - Audio processing engine
- [`PanGuStudio/PanGuStudio/DSP/Spatializer.swift`](../PANGU/PanGuStudio/PanGuStudio/DSP/Spatializer.swift) - 3D spatial audio positioning
- [`PanGuStudio/PanGuStudio/Camera/HandPoseService.swift`](../PANGU/PanGuStudio/PanGuStudio/Camera/HandPoseService.swift) - Hand tracking service
- [`PanGuStudio/PanGuStudio/IO/MIDIClient.swift`](../PANGU/PanGuStudio/PanGuStudio/IO/MIDIClient.swift) - MIDI communication layer

**Vision Processing:**
- [`Vision_Module/mediapipe_dataSet.py`](../PANGU/Vision_Module/mediapipe_dataSet.py) - MediaPipe gesture recognition
- [`Vision_Module/dataToMax.py`](../PANGU/Vision_Module/dataToMax.py) - OSC data transmission to Max/MSP

**Models & Data:**
- [`PanGuStudio/PanGuStudio/Models/GestureModels.swift`](../PANGU/PanGuStudio/PanGuStudio/Models/GestureModels.swift) - Gesture data structures
- [`PanGuStudio/PanGuStudio/Mapping/GestureMapping.swift`](../PANGU/PanGuStudio/PanGuStudio/Mapping/GestureMapping.swift) - Gesture-to-action mapping

#### Next Steps

1. **Testing & Integration**: Connect gesture recognition with audio engine for real-time spatial control
2. **UI Polish**: Complete settings interface and add visual feedback for hand tracking
3. **Performance Optimization**: Fine-tune latency and optimize gesture recognition pipeline
4. **Documentation**: Add code documentation and user guide

### Week 10: Vision Module → Ableton Live Integration (M4L)

This week focused on closing the loop between the MediaPipe vision module and Ableton Live by building the Max for Live device that sits inside the performance set.

#### Key Achievements
- **PanGu.amxd Exported**: Authored and archived the Max for Live audio effect (`Homework/SelfEvaluation/SupportingMaterials/PanGu.amxd`) that hosts the `mc.matrix~` spatial router, `groove~` loop capture, and `live.numbox`/`live.grid` UI for macro control.
- **Gesture-to-Live Mapping**: Verified the OSC stream from `Vision_Module/dataToMax.py` controls six discrete automation lanes in Live with <20 ms round-trip latency.
- **Performance Looping**: Added gesture-triggered `record~`/`groove~` buffers so performers can grab loops and drag them through multichannel space from the depth-camera feed.
- **Documentation Refresh**: Updated the Self-Evaluation packet with new evidence, milestone tracking, and final-performance goals per Homework 4 requirements.

#### Final Target
- Rehearse an eight-minute performance where the depth camera, MediaPipe classifier, and `PanGu.amxd` Max for Live device drive spatial gestures in Ableton Live’s Session View.

---

## Risk & Mitigation
- **Technical (Latency)** → Improve **I/O** paths  
- **Hardware (Endurance)** → **Larger battery** / power optimization  
- **Creative (Outfit/Industrial Design)** → **80/20** approach; better textures & 3D finishes  
- **Project Scope (Too many features)** → Strict **modularization**; stage-gated delivery

---

## Next Steps
- **Repository**: *https://github.com/CharlieSL1/MTEC-498-Capstone.git*  
- **GUI Project**: *https://github.com/CharlieSL1/PanGu-Gesture-and-ML-Based-Control-for-Human-Centered-3D-Audio.git*
- **Self-Evaluation Presentation**: [Google Drive Link](https://drive.google.com/file/d/14qCRTzZLPewIWis8jbfDMorPC7xLenI-/view?usp=sharing)
- **Collaboration**: Open to peer feedback & partnerships  
- **Office Hours**: Mon 1–9 pm; Tue 1–4 pm; Fri 1–6 pm  
- **Email**: cshi@berklee.edu

---

## Beyond This Semester
- **Version 2.0**: Standalone instrument (no computer); **pre-install instruments** for stage use  
- **Scalability**: A **new paradigm** of MIDI keyboard  
- **Team**: EE engineer; product designer; DSP engineer; AI engineer  
- **Commercial Potential**: **Viable as a product**  
- **Research Opportunities**: Explore **creative–AI co-working** and spatial performance cognition

---

## Contact
**Charlie Shi**  
cshi@berklee.edu

---

## Credits
*“Li SHi - Concept Develop and Design.”*

*“Xinyu Li - Sketch & Design”*

*”Special Thanks - Akito van Troyer“*
