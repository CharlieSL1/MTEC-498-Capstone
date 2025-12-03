# PanGu: Spatial Audio Performance Control System
## One-Page Professional Overview

---

### Elevator Pitch

**PanGu** is a next-generation spatial audio performance platform that transforms spatial audio into an expressive instrument. Using depth camera tracking and gesture recognition, performers can intuitively position and manipulate sounds in 3D space in real-time, bridging the gap between technical spatial audio tools and accessible live performance.

---

### Problem Statement

Current music creation and performance tools for spatial audio are either too technical (post-production/DAW-bound) or too experimental (unreliable gestures, weak integration). Musicians lack an intuitive, real-time way to treat sound as a tangible object that can be positioned and performed in space.

---

### Solution

PanGu combines depth camera tracking with gesture recognition to create an intuitive spatial audio performance interface. The system uses:

- **OAK-D Pro Depth Camera**: Provides real-time 3D position tracking (XYZ coordinates)
- **MediaPipe Gesture Recognition**: Recognizes 6 distinct gestures for musical control
- **OSC Communication**: Seamless integration with professional audio software
- **Max for Live Device**: Custom `PanGu.amxd` device for direct Ableton Live control

---

### Key Features

✅ **Real-time 3D Position Tracking** - Accurate XYZ coordinates from depth camera  
✅ **Gesture-Based Control** - 6 gesture types mapped to musical parameters  
✅ **Low Latency Performance** - <20ms round-trip latency for live performance  
✅ **Professional DAW Integration** - Direct control of Ableton Live via Max for Live  
✅ **Modular Architecture** - Clean separation of vision, processing, and audio modules  

---

### Technical Highlights

- **Computer Vision**: MediaPipe-based gesture recognition with real-time processing
- **3D Tracking**: DepthAI pipeline for accurate spatial positioning
- **Real-time Communication**: OSC protocol for low-latency data transmission
- **Audio Integration**: Max/MSP and Max for Live for professional audio processing
- **Performance Optimized**: Thread-safe architecture with efficient data flow

---

### Applications

- **Live Performance**: Expressive instrument for immersive spatial audio shows
- **Studio Production**: Rapid spatial effect testing during composition
- **Art Installations**: Intuitive audience interaction with spatial audio
- **Research**: Platform for exploring gesture-based musical interfaces

---

### Innovation

PanGu bridges cutting-edge spatialization with embodied performance, offering an intuitive, expressive path into immersive sound. The system transforms spatial audio from an engineering task into a playable instrument, making spatial design as immediate as strumming a chord or hitting a drum.

---

### Technology Stack

**Languages**: Python, Max/MSP  
**Libraries**: MediaPipe, DepthAI, python-osc  
**Hardware**: OAK-D Pro depth camera  
**Software**: Ableton Live, Max/MSP, Max for Live  

---

### Future Development

- Standalone instrument version (no computer dependency)
- Expanded gesture vocabulary
- Machine learning-based gesture refinement
- Commercial product development potential
- Research opportunities in spatial audio cognition

---

### Contact & Resources

**Repository**: https://github.com/CharlieSL1/MTEC-498-Capstone.git  
**Course**: MTEC-498: Advanced Projects in Creative Coding  
**Institution**: Berklee College of Music - Electronic Production and Design

---

*This project demonstrates both technical mastery and creative vision, suitable for professional portfolio and industry presentation.*

