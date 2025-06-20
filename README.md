# SHC_project
Repository for the project in the course: Sustainable Heating &amp; Cooling Technologies at ETH. This project's aim is to develop a heat pump system for a pasta cooker related to a student project. The used libraries were introduced in the lecture except for two (but both not directly relevant for the heat pump design). To run the file **`First_Analysis/`** and  **`Finding_Cut_off_for_control/`** the optimizer **Gurobi** as it is our prefered optimizer and we wanted to get an idea of the problem as fast as possible (**Gurobi** with very low runtime).

---
## Project Structure

- **`First_Analysis/`**: Contains a thorough analysis of the stated problems. Several scenarios were simulated and optimized for, to get a good idea of the system's dynamics. 
- **`main/`**: Contains the heat pump design. The design is optimized for different compressor tube diameters and refrigerants, where one configuration was chosen. The operation strategy for the chosen configuration is also included. 
- **`functions/`**: Contains the functions needed for the heat pump design and analysis.
- **`Finding_Cut_off_for_control/`**: Contains the scenario analysis which is introduced in **`First_Analysis/`**. It stores the data needed for the controlling system in **`controlling_temperature_off_for_fixed_Q/`**.
- **`controlling_temperature_off_for_fixed_Q/`**: Contains the temperature data at which the heat pump is to be turned off depending on the nominal power (used for heat pump design selection see in **`main/`**).
- **`results/`**: Contains the csv files with the results.
- **`figures/`**: Contains the figures used in the report.
- **`requirements.txt`**: Lists all Python packages required to run the code.

---

## Setup Instructions

To get started, set up a virtual environment (optional but recommended) and install dependencies:

```bash
# Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

---

## Results


---

## Contributors

- Alessio Häseli
- Simon Bernet

## Estimated Runtime


```

