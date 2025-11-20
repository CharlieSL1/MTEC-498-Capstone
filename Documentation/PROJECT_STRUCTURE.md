# PanGu Project Structure

This document outlines the organized structure of the MTEC-498-Capstone project.

## Directory Structure

```
MTEC-498-Capstone/
├── README.md                    # Main project documentation
├── Documentation/               # Docs and structure guide
│   └── PROJECT_STRUCTURE.md     # This file - project organization guide
├── .gitignore                   # Git ignore rules for sensitive files
├── assets/                      # Centralized asset storage
│   ├── images/                  # Project images and diagrams
│   │   ├── SystemFlow.png       # System flow diagram
│   │   └── V2.png               # V2 concept diagram
│   └── documents/               # Project documents and keys
│       └── PANGUV2.pdf          # Version 2 project document
├── Homework/                    # Course homework and assignments
│   ├── PeerReview/              # Peer review materials
│   ├── ProgressReport/          # Progress report materials
│   ├── ProjectProposal/         # Initial project proposal materials
│   │   ├── PanGu_V1.jpg         # Version 1 concept image
│   │   ├── PanGu.pdf            # Project proposal PDF
│   │   ├── PanGu.png            # Project flow chart
│   │   └── README.md            # Proposal documentation
│   └── SelfEvaluation/          # Self evaluation materials
├── Project/                     # Weekly progress snapshots
│   ├── Week3/                   # Week 3 progress and documentation
│   │   ├── README.md            # Week 3 progress report
│   │   └── README.ipynb         # Jupyter notebook for Week 3
│   ├── Week4/                   # Week 4 progress and documentation
│   │   └── README.md            # Week 4 progress report
│   ├── Week6/                   # Week 6 code drop (vision + Max patch)
│   │   ├── Max_Module/          # Max patch used that week
│   │   ├── Vision_Module/       # Gesture pipeline and OSC sender
│   │   ├── README.md            # Week 6 notes
│   │   └── main.py              # Week 6 entry script
│   └── Week11/                  # Week 11 updated depth + Max for Live snapshot
│       ├── Max_Audio_Effect/    # Ableton/Max for Live device
│       ├── Vision_Module/       # DepthAI + gesture modules
│       ├── README.md            # Week 11 progress notes
│       └── main.py              # Week 11 entry script
```

## File Organization Principles

1. **Centralized Assets**: All images and documents are stored in the `assets/` directory
2. **Weekly Documentation**: Each week's progress is documented in its own directory
3. **Sensitive Files**: Key files and sensitive documents are stored in `assets/documents/` and gitignored
4. **Clean Root**: The root directory contains only essential project files
5. **Consistent Naming**: All files follow consistent naming conventions

## Asset Management

- **Images**: Store all project images, diagrams, and visual assets in `assets/images/`
- **Documents**: Store PDFs, keys, and other documents in `assets/documents/`
- **References**: Update README files to reference assets using relative paths from their location

## Git Management

- Sensitive files (`.key`, `.pem`, etc.) are automatically ignored
- OS-generated files are ignored
- IDE and build files are ignored
- Only source code and documentation are tracked

## Weekly Progress

Each week's directory contains:
- `README.md`: Progress report and decisions made
- Any week-specific assets or code
- Links to relevant external resources

## Maintenance

- Keep the root directory clean by moving new assets to appropriate subdirectories
- Update this structure document when adding new directories or reorganizing
- Ensure all README files reference assets using correct relative paths
