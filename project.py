import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Main function to interact with the user and calculate beam deflection and bending moment.
    """
    while True:
        print("\nBeam Deflection and Bending Moment Calculator")

        beam_types = {
            "1": "simply_supported",
            "2": "cantilever"
        }

        load_types = {
            "1": "point_load",
            "2": "uniformly_distributed"
        }

        # Select beam type
        print("Select the beam type:")
        print("1. Simply Supported Beam")
        print("2. Cantilever Beam")
        beam_choice = input("Enter your choice (1/2): ").strip()
        beam_type = beam_types.get(beam_choice)

        if not beam_type:
            print("Invalid choice. Exiting.")
            return

        # Select load type
        print("\nSelect the load type:")
        print("1. Point Load")
        print("2. Uniformly Distributed Load (UDL)")
        load_choice = input("Enter your choice (1/2): ").strip()
        load_type = load_types.get(load_choice)

        if not load_type:
            print("Invalid choice. Exiting.")
            return

        # Gather beam properties
        L = get_numeric_input("\nEnter the span length of the beam (m): ", positive_only=True)
        print("Reminder: Modulus of Elasticity (E) is typically very large. For steel, it's usually around 200 GPa (200e9 Pa).")
        E = get_numeric_input("Enter the modulus of elasticity (Pa): ", positive_only=True)
        I = get_numeric_input("Enter the moment of inertia (m^4): ", positive_only=True)

        # Load details
        P, w = 0, 0
        if load_type == "point_load":
            P = get_numeric_input("Enter the magnitude of the point load (N): ", positive_only=True)
        elif load_type == "uniformly_distributed":
            w = get_numeric_input("Enter the load per unit length (N/m): ", positive_only=True)

        # Calculate deflection and bending moment
        delta_max_m = calculate_deflection(beam_type, load_type, P, w, L, E, I)
        M_max = calculate_bending_moment(beam_type, load_type, P, w, L)

        delta_max_cm = delta_max_m * 100

        # Display results
        print(f"\nThe maximum deflection is: {delta_max_cm:.6f} centimeters")
        print(f"The maximum bending moment is: {M_max:.2f} Nm")

        # Plot the deflection curve
        plot_beam(beam_type, load_type, L, delta_max_m)

        # Input to run another calculation
        another_run = input("\nWould you like to calculate another beam deflection? (y/n): ").strip().lower()
        if another_run != 'y':
            print("Exiting the program. Thank you!")
            break


def calculate_deflection(beam_type: str, load_type: str, P: float, w: float, L: float, E: float, I: float) -> float:
    """
    Calculate the maximum deflection for a given beam and load type.
    """
    if beam_type == "simply_supported":
        if load_type == "point_load":
            return (P * L**3) / (48 * E * I)
        elif load_type == "uniformly_distributed":
            return (5 * w * L**4) / (384 * E * I)
    elif beam_type == "cantilever":
        if load_type == "point_load":
            return (P * L**3) / (3 * E * I)
        elif load_type == "uniformly_distributed":
            return (w * L**4) / (8 * E * I)
    raise ValueError(f"Invalid beam type '{beam_type}' or load type '{load_type}'.")


def calculate_bending_moment(beam_type: str, load_type: str, P: float, w: float, L: float) -> float:
    """
    Calculate the maximum bending moment for a given beam and load type.

    Args:
        beam_type (str): Type of the beam ("simply_supported" or "cantilever").
        load_type (str): Type of the load ("point_load" or "uniformly_distributed").
        P (float): Magnitude of the point load in Newtons (N).
        w (float): Magnitude of the uniformly distributed load in Newtons per meter (N/m).
        L (float): Span length of the beam in meters (m).

    Returns:
        float: Maximum bending moment in Newton-meters (Nm).
    """
    if beam_type == "simply_supported":
        if load_type == "point_load":
            return P * L / 4
        elif load_type == "uniformly_distributed":
            return w * L**2 / 8
    elif beam_type == "cantilever":
        if load_type == "point_load":
            return P * L
        elif load_type == "uniformly_distributed":
            return w * L**2 / 2
    raise ValueError(f"Invalid beam type '{beam_type}' or load type '{load_type}'.")


def plot_beam(beam_type: str, load_type: str, L: float, delta_max: float):
    """
    Plot the deflection curve for the beam.
    """
    x = np.linspace(0, L, 500)

    if beam_type == "simply_supported":
        if load_type == "point_load":
            deflection = (delta_max / (L / 2)**3) * (-x**3 + L * x**2)
        elif load_type == "uniformly_distributed":
            deflection = (delta_max / (L**4)) * (-x**4 + 2 * L * x**3 - L**2 * x**2)
    elif beam_type == "cantilever":
        if load_type == "point_load":
            deflection = (delta_max / L**3) * (x**3 - 3 * L * x**2 + 2 * L**2 * x)
        elif load_type == "uniformly_distributed":
            deflection = (delta_max / L**4) * (x**4 - 4 * L * x**3 + 6 * L**2 * x**2)

    plt.plot(x, deflection, label="Deflection Curve")
    plt.axhline(0, color="black", linewidth=1)
    plt.title(f"Beam Deflection: {beam_type.replace('_', ' ').title()} with {load_type.replace('_', ' ').title()}")
    plt.xlabel("Length along the Beam (m)")
    plt.ylabel("Deflection (m)")
    plt.legend()
    plt.grid(True)
    plt.savefig("beam_deflection.png")
    print("Deflection plot saved as 'beam_deflection.png'.")
    plt.show()
    plt.close()


def get_numeric_input(prompt: str, positive_only: bool = False) -> float:
    """
    Get validated numeric input from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if positive_only and value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    main()
