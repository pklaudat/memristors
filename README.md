# Memristors
This project aims to be a collaborative effort to collect memristor models published in the literature adapted to Cadence Spectre Simulator. The contribution of your models are welcome and there is a reference to each model presented.

if you are interested in using one of these models in your work, remember to use their respective references to cite them.
## Repository Structure
    .
    ├── micromagnetic simulation # free layer model of spintronic memristors (IMTJ)
    ├── spice                    # SPICE models of Memristors
    │   ├── biolek                 # Biolek Model - In Progress... (not ready for usage) 
    │   ├── c-spin IMTJ            # UMN IMTJ model refactored to Spectre Synthax
    │   ├── c-spin PMTJ            # UMN PMTJ model with few changes in Resistor module
    │   ├── current-threshold      # Current-threshold Memristor (based on Pershin and Di Ventra - UFRGS)
    │   └── verilog PMTJ           # A verilog model of PMTJ (ARM)
    └── ...

