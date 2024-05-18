import random
import curses
import time
import numpy as np
from collections import defaultdict

# Constants for particle types
PARTICLES = [
    "Electron", "Positron", "Quark", "Anti-Quark", 
    "Photon", "Neutrino", "Anti-Neutrino", "Muon", "Anti-Muon"
]

# Particle masses (in GeV/c^2)
PARTICLE_MASSES = {
    "Electron": 0.000511,
    "Positron": 0.000511,
    "Quark": 0.005,  # Simplified average mass for light quarks
    "Anti-Quark": 0.005,
    "Photon": 0.0,
    "Neutrino": 1e-9,  # Very small mass for neutrinos
    "Anti-Neutrino": 1e-9,
    "Muon": 0.105,
    "Anti-Muon": 0.105
}

# Define the volume of space (in cubic meters)
VOLUME = 1  # 1 cubic meter

# Initialize particle counts
particle_counts = defaultdict(int)
total_particle_counts = defaultdict(int)
total_energy = 0.0
total_momentum = defaultdict(float)
total_lifetime = defaultdict(float)
total_energy_spectrum = defaultdict(list)
total_temperature = 0.0
total_density_fluctuations = 0.0
total_cross_sections = {}
total_boundary_effects = defaultdict(float)
total_gravitational_effects = defaultdict(float)
total_experiment_comparison = 0.0
total_interactions = 0
time_steps = 0

def zero_point_energy(mass):
    """
    Calculate the zero-point energy of a quantum harmonic oscillator.
    E_0 = (1/2) * hbar * omega
    Here, omega = sqrt(k/m) and k is approximated by m * c^2 for simplicity.
    """
    c = 3e8  # Speed of light in m/s
    hbar = 6.582119569e-25  # Reduced Planck constant in GeV*s
    omega = c * np.sqrt(mass)
    return 0.5 * hbar * omega

def simulate_vacuum_energy():
    """
    Simulates the vacuum energy field and the potential for virtual particle pair creation.
    """
    global total_energy, total_momentum, total_lifetime, total_energy_spectrum
    global total_temperature, total_density_fluctuations, total_cross_sections
    global total_boundary_effects, total_gravitational_effects, total_experiment_comparison
    global total_interactions, time_steps

    # Randomly decide whether a particle pair is created or annihilated
    action = random.choice(["create", "annihilate"])
    particle_type = random.choice(PARTICLES[:-1])  # Exclude photons from creation/annihilation

    if action == "create":
        particle_counts[particle_type] += 1
        total_particle_counts[particle_type] += 1
    elif action == "annihilate" and particle_counts[particle_type] > 0:
        particle_counts[particle_type] -= 1
        if particle_type in ["Electron", "Positron", "Quark", "Anti-Quark", "Muon", "Anti-Muon"]:
            particle_counts["Photon"] += 2  # Pair annihilation produces photons
            total_particle_counts["Photon"] += 2
        total_interactions += 1

    # Calculate the vacuum energy
    current_energy = sum(zero_point_energy(PARTICLE_MASSES[pt]) * count for pt, count in particle_counts.items())
    total_energy += current_energy

    # Calculate momentum distribution
    for pt, count in particle_counts.items():
        total_momentum[pt] += np.sqrt(2 * zero_point_energy(PARTICLE_MASSES[pt]) / VOLUME)

    # Calculate average particle lifetime
    for pt, count in particle_counts.items():
        total_lifetime[pt] += 1 / (count + 1)  # Simple approximation

    # Calculate energy spectrum
    for pt, count in particle_counts.items():
        total_energy_spectrum[pt].append(zero_point_energy(PARTICLE_MASSES[pt]))

    # Calculate temperature (average energy per degree of freedom)
    total_temperature += current_energy / len(particle_counts)  # Approximation

    # Calculate density fluctuations (standard deviation of particle counts)
    total_density_fluctuations += np.std(list(particle_counts.values()))

    # Calculate interaction cross-sections (sum of all particle counts)
    total_cross_sections[time_steps] = sum(particle_counts.values())

    # Calculate boundary effects (e.g., confinement effects)
    total_boundary_effects[time_steps] = 0.0  # Placeholder for future implementation

    # Calculate gravitational effects (e.g., gravitational redshift)
    total_gravitational_effects[time_steps] = 0.0  # Placeholder for future implementation

    # Calculate comparison with experimental data or theoretical predictions
    total_experiment_comparison += 0.0  # Placeholder for future implementation

    time_steps += 1

    return current_energy / VOLUME  # Scale energy to per cubic meter

def display_vacuum_simulation(stdscr):
    """
    Displays the vacuum energy field simulation using curses.
    """
    time_step = 0
    while True:
        stdscr.clear()

        # Simulate vacuum energy field
        current_energy = simulate_vacuum_energy()
        average_energy = total_energy / (time_steps * VOLUME)

        # Display the current state
        stdscr.addstr(0, 0, f"Time Step: {time_step}")
        stdscr.addstr(1, 0, f"{'Particle':<15} | {'Count':<10} | {'Total Count':<12} | {'Zero-point Energy (GeV)':<25}")
        stdscr.addstr(2, 0, "-" * 65)

        for i, particle in enumerate(PARTICLES, start=3):
            count = particle_counts[particle]
            total_count = total_particle_counts[particle]
            zpe = zero_point_energy(PARTICLE_MASSES[particle]) * count
            stdscr.addstr(i, 0, f"{particle:<15} | {count:<10} | {total_count:<12} | {zpe:<25.6e}")

        stdscr.addstr(i + 2, 0, f"Current Vacuum Energy (per cubic meter): {current_energy:.6e} GeV")
        stdscr.addstr(i + 3, 0, f"Average Vacuum Energy (per cubic meter): {average_energy:.6e} GeV")
        stdscr.addstr(i + 4, 0, f"Total Interactions: {total_interactions}")

        # Refresh the screen
        stdscr.refresh()

        # Sleep for a short time before the next update
        time.sleep(0.1)

        # Increment time step
        time_step += 1

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    display_vacuum_simulation(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
