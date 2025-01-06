# Beam Deflection and Bending Moment Calculator
#### Video Demo: (https://youtu.be/DnYeEq2zpTs)

## Description:
This Python project calculates the maximum deflection and bending moment for different types of beams subjected to various loading conditions. The user can select the beam type (simply supported or cantilever) and the load type (point load or uniformly distributed load) and provide the necessary parameters, such as the span length, modulus of elasticity, and moment of inertia.

### Key Features:
- **Deflection Calculation**: Computes the maximum deflection of the beam based on its type, load type, and physical properties.
- **Bending Moment Calculation**: Computes the maximum bending moment for the beam using the same input parameters.
- **Interactive Input**: Users are prompted to input beam properties such as span length, modulus of elasticity, and moment of inertia.
- **Graph Plotting**: The deflection curve is plotted and saved as an image (`beam_deflection.png`).
- **Error Handling**: The program includes robust input validation and error handling for incorrect or invalid inputs.

### Project Structure:
The project consists of the following key files:
- `project.py`: Contains the main logic of the program, including functions for calculating beam deflection and bending moment, as well as plotting the deflection curve.
- `test_project.py`: Contains test cases implemented using `pytest` to ensure the correctness of the core functions. This includes tests for the deflection and bending moment calculations and input validation.
- `requirements.txt`: Lists the required dependencies for running the project.

### Functions:
1. **main()**:
   - Handles user input, calls the calculation functions, and prints the results.

2. **calculate_deflection(beam_type, load_type, P, w, L, E, I)**:
   - Calculates the maximum deflection of the beam based on beam type, load type, and given physical properties.

3. **calculate_bending_moment(beam_type, load_type, P, w, L)**:
   - Calculates the maximum bending moment of the beam based on the input parameters.

4. **plot_beam(beam_type, load_type, L, delta_max)**:
   - Plots the deflection curve and saves it as an image (`beam_deflection.png`).

5. **get_numeric_input(prompt, positive_only)**:
   - Prompts the user for numeric input and validates the input.

### Installation and Usage:
To use the program, follow these steps:
1. Clone or download the project repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
