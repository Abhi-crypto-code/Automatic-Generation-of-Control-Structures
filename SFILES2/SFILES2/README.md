# PFDtoP&ID - Automated Control Structure Generation

This repository focuses on extending the SFILES2 framework for automating the generation of control structures (P&IDs) from process flow diagrams (PFDs).

## Objective

To explore and improve the workflow from Process Flow Diagrams (PFDs) to Piping & Instrumentation Diagrams (P&IDs) by:
- Understanding the SFILES framework and its notation.
- Improving graph visualization and layout.
- Analyzing simulation software formats like DWSIM for usable data.
- Evaluating LLM and ML-based approaches for graph extraction.

## Weekly Progress Summary

### Understanding the Research
- Read the main paper on SFILES and its application in control structure generation.
- Studied the notation and representation of flowsheets using the SFILES language.

### Codebase and Graph Generation
- Explored the SFILES2 codebase and its graph generation pipeline.
- Worked with `networkx` to enhance graph readability:
  - Compared different layouts (planar, spring).
  - Dynamically scaled node size, font size, arrow width, and opacity based on the number of nodes.

### File Format Investigation
- Analyzed DWSIM's file structure:
  - XML and compressed XML store data as nested dictionaries.
  - Investigated `.pfdx` format as a potential source for graph representation.

### ML and LLM-Based Approaches
- Explored CNN-based image-to-graph conversion literature.
- Evaluated some LLM-generated outputs against expected SFILES structures.

## Tools and Libraries Used

- Python
- NetworkX
- Matplotlib
- DWSIM
- SFILES2 framework

## Directory Structure

```bash
.
├── data/                     # Raw input and simulation files
├── graphs/                   # Generated graph visualizations
├── SFILES2/                  # Codebase related to SFILES implementation
├── notebooks/                # Jupyter notebooks for experiments
├── outputs/                  # LLM outputs and comparisons
├── PFDtoP&ID.pdf             # Reference research material
└── README.md                 # This file

