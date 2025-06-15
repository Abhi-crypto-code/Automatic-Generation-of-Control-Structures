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


# Week 2 Progress

## 🚧 Focus Areas
- Parsing DWSIM XML files and converting to graph structures
- Deep understanding of SFILES2 notation and its physical interpretation
- Graph visualization improvements (controller/transmitter styling)
- Initial exploration of vision-based tools (Ollama, LLaVA) for image-to-graph ideas
- Consultations with mentors and the original paper author

---

## 🔧 Technical Work
- Implemented algorithm to convert DWSIM `.xml` files → `.graphml`
- Successfully visualized flowsheet graphs using NetworkX
- Solved GUID issue (e.g., `MAT-1579...`) by mapping to readable unit operation names
- Enhanced graph visuals: color-coded controllers, scaled nodes/labels/arrows
- Manually dry-ran and understood small SFILES2 examples

---

## Next Steps
- Finalize end-to-end pipeline: XML → Graph → SFILES2
- Automate SFILES2 generation from graphs
- Validate outputs against real PFDs/P&IDs
- Begin basic UI for visualization and model integration

# Weekly Progress Summary - 2

## Work Done
- Discussed direction of work with Priyam Sir and Prof. Arthur (research author).
- Developed algorithm to convert `.xml` files to `.graphml` and successfully plotted the graph.
- Implemented basic graph coloring for notation clarity.
- Created algorithm to count unit operations, controllers, and indicators.
- Explored LLaMA Vision to interpret physical meaning from P&ID-like images.
- Studied SFILES notation and underlying algorithm.
- Looked into SMILES notation for future applicability.

##  Issues Faced
- GUID-based tags (e.g., `[MAT-xxxxx]`) lack readable unit names.
  - Explored mapping solutions; C#/.NET API found impractical.
  - Need a consistent GUID-to-name conversion method.
- Failed attempt to compare overall graph structures via edge comparison.
  - Controllers inserted between paths disrupt direct matching.
  - Requires alternative structural comparison algorithm.
- Struggled with physical interpretation of process/controllers in presentation.

