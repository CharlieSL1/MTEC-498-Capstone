# PanGu Project Structure

This document outlines the organized structure of the MTEC-498-Capstone project.

## Directory Structure

```
MTEC-498-Capstone/
├── README.md                    # Main project documentation
├── PROJECT_STRUCTURE.md         # This file - project organization guide
├── .gitignore                   # Git ignore rules for sensitive files
├── assets/                      # Centralized asset storage
│   ├── images/                  # All project images and diagrams
│   │   ├── SystemFlow.png       # Week 4 system flow diagram
│   │   └── V2.png              # Week 3 V2 concept diagram
│   └── documents/              # Project documents and keys
│       ├── PANGUV2.pdf         # Version 2 project document
│       └── PANGU.key           # Project key file (gitignored)
├── Homework/                   # Course homework and assignments
│   └── ProjectProposal/        # Initial project proposal materials
│       ├── PanGu_V1.jpg        # Version 1 concept image
│       ├── PanGu.pdf           # Project proposal PDF
│       ├── PanGu.png           # Project flow chart
│       └── README.md           # Proposal documentation
├── Week3/                      # Week 3 progress and documentation
│   ├── README.md               # Week 3 progress report
│   └── README.ipynb           # Jupyter notebook for Week 3
└── Week4/                      # Week 4 progress and documentation
    └── README.md               # Week 4 progress report
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

