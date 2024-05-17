

# Galaxy Simulation Scripts

This repository contains two Python scripts for simulating galaxy dynamics using the `curses` library for real-time visualization in the terminal. The first script simulates galaxy rotation velocities using Newtonian and MOND gravity theories. The second script simulates galaxy formation and mass density evolution against cosmic inflation, incorporating various astrophysical processes.

## Scripts Overview

### 1. Galaxy Rotation Simulation

**Script:** `galaxy_rotation.py`

This script simulates and visualizes the rotational velocities of a galaxy using both Newtonian and MOND (Modified Newtonian Dynamics) gravity models. It accounts for dark matter density profiles, gas density profiles, and stellar populations.

#### Features:
- Real-time simulation of galaxy rotation velocities.
- Visualization of Newtonian and MOND velocities.
- Inclusion of dark matter and gas density profiles.
- Dynamic mass changes over time.
- Visualization using the `curses` library.

#### Usage:
1. **Install necessary libraries**:
   ```sh
   pip install numpy
   ```
2. **Run the script**:
   ```sh
   python galaxy_rotation.py
   ```

### 2. Galaxy Formation and Density Simulation

**Script:** `galaxy_formation_density.py`

This script simulates and visualizes the formation and density evolution of a galaxy over time, considering cosmic inflation, gas accretion, gas ejection, star formation, star death, black hole formation, and dark matter halo growth.

#### Features:
- Real-time simulation of galaxy formation and mass density.
- Visualization of current and average values for inflation factor, galaxy formation rate, and mass density.
- Dynamic update of total mass, stellar mass, black hole mass, gas mass, and dark matter mass.
- Visualization using the `curses` library.

#### Usage:
1. **Install necessary libraries**:
   ```sh
   pip install numpy
   ```
2. **Run the script**:
   ```sh
   python galaxy_formation_density.py
   ```

## Detailed Explanation

### Galaxy Rotation Simulation

The `galaxy_rotation.py` script computes the rotational velocities of a galaxy at various radii using both Newtonian and MOND theories. It incorporates the following components:

- **Dark Matter Density Profile**: Affects the gravitational potential and thus the rotation curve.
- **Gas Density Profile**: Contributes to the mass distribution and affects the rotation curve.
- **Stellar Populations**: Different populations of stars with varying formation rates and lifetimes.

#### Functions:
- `rotational_velocity_newton(radius, mass)`: Computes rotational velocities using Newtonian gravity.
- `rotational_velocity_mond(radius, mass)`: Computes rotational velocities using MOND.
- `simulate_galaxy_rotation(radius, mass, ...)`: Simulates the rotation using both theories, incorporating dark matter and gas profiles.
- `display_galaxy_rotation(stdscr, radius, ...)`: Visualizes the results in the terminal using `curses`.

### Galaxy Formation and Density Simulation

The `galaxy_formation_density.py` script simulates galaxy formation and mass density evolution over time, taking into account various astrophysical processes. It includes:

- **Cosmic Inflation**: Affects the mass density of the universe.
- **Star Formation**: New stars form from gas.
- **Star Death and Black Hole Formation**: Stars die and some form black holes.
- **Gas Accretion and Ejection**: Gas is added to and removed from the galaxy.
- **Dark Matter Halo Growth**: Dark matter mass increases over time.

#### Functions:
- `simulate_galaxy_formation_and_density(time_step, ...)`: Computes the evolution of mass components and density.
- `display_galaxy_formation_and_density(stdscr)`: Visualizes the simulation in the terminal using `curses`.

## Additional Information

### Dependencies

- Python 3.x
- NumPy
- Curses (part of Python standard library)

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


```
