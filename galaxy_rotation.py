import numpy as np
import time
import os

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
a_0 = 1e-10  # critical acceleration scale parameter (m/s^2)

# Define the NFW dark matter density profile
def nfw_density_profile(radius, scale_radius, rho_0):
    x = radius / scale_radius
    return rho_0 / (x * (1 + x) ** 2)

# Function to calculate gravitational potential due to dark matter
def dark_matter_potential(radius, scale_radius, rho_0):
    potential = -4 * np.pi * G * rho_0 * scale_radius**2 * (
        np.log(1 + radius / scale_radius) - radius / (radius + scale_radius)
    )
    return potential

# Function to calculate rotational velocity due to dark matter
def rotational_velocity_dark_matter(radius, scale_radius, rho_0):
    potential = dark_matter_potential(radius, scale_radius, rho_0)
    velocity = np.sqrt(-potential / radius)
    return velocity

# Function to calculate rotational velocity using Newtonian gravity
def rotational_velocity_newton(radius, mass):
    return np.sqrt(G * mass / radius)

# Gas density profile function
def gas_density_profile(radius):
    return 1e8 / (radius + 1)

# Function to simulate rotation of a galaxy including dark matter, dynamical mass variation, gas dynamics, and multiple stellar populations
def simulate_galaxy_rotation(radius, initial_mass, dark_matter_scale_radius, dark_matter_rho_0, gas_density_profile, time_step, mass_change_rate, stellar_population, gas_mass, stellar_mass):
    current_mass = initial_mass
    while True:
        newtonian_velocities = rotational_velocity_newton(radius, current_mass + gas_mass + np.sum(list(stellar_mass.values()), axis=0))
        dark_matter_velocities = rotational_velocity_dark_matter(radius, dark_matter_scale_radius, dark_matter_rho_0)
        total_velocities = np.sqrt(newtonian_velocities**2 + dark_matter_velocities**2)
        yield total_velocities
        # Update mass for the next time step
        gas_mass += mass_change_rate * time_step  # Gas accretion rate
        star_formation_rate = 0.01 * gas_mass  # Star formation efficiency
        for name, properties in stellar_population.items():
            stellar_mass_change = properties['formation_rate'] * time_step
            stellar_mass[name] += stellar_mass_change  # Increase in stellar mass
            gas_mass -= stellar_mass_change  # Depletion of gas mass
        current_mass += mass_change_rate * time_step  # Increase in total mass

# Function to display galaxy rotation including details for each factor
def display_galaxy_rotation(radius, initial_mass, dark_matter_scale_radius, dark_matter_rho_0, gas_density_profile_name, time_step, mass_change_rate, stellar_population, gas_mass, stellar_mass):
    simulation = simulate_galaxy_rotation(radius, initial_mass, dark_matter_scale_radius, dark_matter_rho_0, gas_density_profile, time_step, mass_change_rate, stellar_population, gas_mass, stellar_mass)
    t = 0
    while True:
        total_velocities = next(simulation)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"Time Step: {t}")
        print("Radius (kpc) | Total Velocity (km/s)")
        print("-" * 40)
        for r, v_total in zip(radius, total_velocities):
            print(f"{r:10.2f} | {v_total:20.2f}")
        print("\nAdditional Information:")
        print(f"Dark Matter Scale Radius: {dark_matter_scale_radius} kpc")
        print(f"Dark Matter Central Density: {dark_matter_rho_0} kg/m^3")
        print(f"Gas Density Profile: {gas_density_profile_name}")
        print(f"Time Step: {time_step} arbitrary units")
        print(f"Mass Change Rate: {mass_change_rate} kg/time step")
        print("Stellar Populations:")
        for name, properties in stellar_population.items():
            print(f"- {name}:")
            print(f"  - Star Formation Rate: {properties['formation_rate']} (arbitrary units)")
            print(f"  - Mass: {np.sum(stellar_mass[name])} kg")
        print(f"Total Galaxy Mass: {np.sum(initial_mass) + gas_mass + np.sum([np.sum(m) for m in stellar_mass.values()])} kg")
        time.sleep(0.1)  # Adjust sleep time as needed
        t += 1

# Function to add a new stellar population
def add_stellar_population(stellar_population, name, formation_rate):
    stellar_population[name] = {'formation_rate': formation_rate}

# Function to remove a stellar population
def remove_stellar_population(stellar_population, name):
    del stellar_population[name]

# Run simulation including dark matter, dynamical mass variation, gas dynamics, and multiple stellar populations
def main():
    # Parameters
    radius = np.linspace(1, 10, 10)  # radius of the galaxy (kpc)
    initial_mass = 1e12  # initial mass of the galaxy (kg)
    dark_matter_scale_radius = 5  # scale radius of dark matter halo (kpc)
    dark_matter_rho_0 = 1e9  # central density of dark matter halo (kg/m^3)
    time_step = 1  # time step (arbitrary units)
    mass_change_rate = 1e10  # rate of change of mass per time step (kg/time step)
    
    # Define properties of multiple stellar populations
    stellar_population = {
        'Population 1': {'formation_rate': 0.001},  # Example star formation rate for Population 1
        'Population 2': {'formation_rate': 0.002}   # Example star formation rate for Population 2
        # Add more populations as needed
    }

    # Initial gas mass and stellar mass for each population
    gas_mass = 0
    stellar_mass = {name: np.zeros_like(radius) for name in stellar_population}

    # Display galaxy rotation including dark matter, dynamical mass variation, gas dynamics, and multiple stellar populations
    display_galaxy_rotation(radius, initial_mass, dark_matter_scale_radius, dark_matter_rho_0, gas_density_profile.__name__, time_step, mass_change_rate, stellar_population, gas_mass, stellar_mass)

if __name__ == "__main__":
    main()
