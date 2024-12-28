import random
import curses
import time
import numpy as np
from collections import defaultdict

# Constants
c = 3e8  # Speed of light (m/s)
hbar = 6.582119569e-25  # Reduced Planck constant (GeV*s)
k_b = 8.617333262145e-5  # Boltzmann constant (GeV/K)
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)

# Particle Data
PARTICLES = {
    "Electron": {"mass": 0.000511, "charge": -1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Positron": {"mass": 0.000511, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Muon": {"mass": 0.105, "charge": -1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Anti-Muon": {"mass": 0.105, "charge": +1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Neutron": {"mass": 0.939, "charge": 0, "spin": 0.5, "lifetime": 880.2, "type": "fermion"},
    "Proton": {"mass": 0.938, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Photon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson"},
    "Gluon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson"},
    "W Boson": {"mass": 80.379, "charge": +1, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Z Boson": {"mass": 91.1876, "charge": 0, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Higgs Boson": {"mass": 125.1, "charge": 0, "spin": 0, "lifetime": 1.56e-22, "type": "boson"},
    "Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Tau": {"mass": 1.777, "charge": -1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
    "Anti-Tau": {"mass": 1.777, "charge": +1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
}

# Decay Channels
DECAY_CHANNELS = {
    "Muon": [("Electron", "Electron Neutrino", "Muon Neutrino")],
    "Tau": [("Muon", "Muon Neutrino", "Tau Neutrino"), ("Electron", "Electron Neutrino", "Tau Neutrino")],
    "Neutron": [("Proton", "Electron", "Electron Neutrino")],
    "W Boson": [("Electron", "Electron Neutrino"), ("Muon", "Muon Neutrino"), ("Tau", "Tau Neutrino")],
    "Z Boson": [("Electron", "Positron"), ("Muon", "Anti-Muon")],
}

# Interaction Channels
INTERACTION_CHANNELS = {
    ("Proton", "Neutron"): [("Deuterium", "Photon")],  # Fusion
    ("Electron", "Positron"): [("Photon", "Photon")],  # Annihilation
    ("Photon", "Electron"): [("Photon", "Electron")],  # Scattering
}

# Simulation Variables
MODE = "Default"
VOLUME = 1.0
particle_counts = defaultdict(int)
total_energy = 0.0
temperature = 2.7
entropy = 0.0
time_steps = 0
time_delay = 0.1
timestep_multiplier = 1
total_particles_created = 0
total_particles_decayed_natural = 0
total_particles_decayed_interaction = 0


def zero_point_energy(mass):
    """Calculate zero-point energy for a particle."""
    omega = c * np.sqrt(mass)
    return 0.5 * hbar * omega


def relativistic_energy(mass, speed):
    """Calculate relativistic energy."""
    gamma = 1 / np.sqrt(1 - (speed ** 2) / (c ** 2))
    return gamma * mass * c**2


def decay_particle(particle):
    """Handle particle decay."""
    global total_particles_decayed_natural
    if particle in DECAY_CHANNELS and particle_counts[particle] > 0:
        particle_counts[particle] -= 1
        total_particles_decayed_natural += 1
        for product in random.choice(DECAY_CHANNELS[particle]):
            particle_counts[product] += 1


def handle_interactions():
    """Handle particle interactions."""
    global total_particles_decayed_interaction
    particle_pairs = list(INTERACTION_CHANNELS.keys())
    for pair in particle_pairs:
        if particle_counts[pair[0]] > 0 and particle_counts[pair[1]] > 0:
            if random.random() < 0.01:  # Interaction probability
                particle_counts[pair[0]] -= 1
                particle_counts[pair[1]] -= 1
                products = random.choice(INTERACTION_CHANNELS[pair])
                for product in products:
                    particle_counts[product] += 1
                total_particles_decayed_interaction += 1


def radiation_density():
    """Calculate radiation density."""
    global total_energy
    photon_count = particle_counts.get("Photon", 0)
    energy_per_photon = hbar * c / 1e-7  # Assume average photon wavelength of 1e-7 m
    return photon_count * energy_per_photon / VOLUME


def gravitational_potential():
    """Calculate gravitational potential energy."""
    total_potential = 0
    for p1, c1 in particle_counts.items():
        for p2, c2 in particle_counts.items():
            if p1 != p2:
                r = random.uniform(1e-10, 1e-3)  # Random distance between particles
                total_potential += -G * PARTICLES[p1]["mass"] * PARTICLES[p2]["mass"] * c1 * c2 / r
    return total_potential


def simulate_vacuum_energy(adjusted_timestep):
    """Simulates particle interactions."""
    global total_energy, entropy, temperature, time_steps, total_particles_created, total_particles_decayed_interaction, VOLUME

    # Particle creation/annihilation
    particle_type = random.choice(list(PARTICLES.keys()))
    action = random.choice(["create", "annihilate"])
    if action == "create":
        particle_counts[particle_type] += 1
        total_particles_created += 1
    elif action == "annihilate" and particle_counts[particle_type] > 0:
        particle_counts[particle_type] -= 1
        total_particles_decayed_interaction += 1

    # Handle particle decay
    for particle, count in list(particle_counts.items()):
        if count > 0 and PARTICLES[particle]["lifetime"] < 1e30:
            if random.random() < adjusted_timestep / PARTICLES[particle]["lifetime"]:
                decay_particle(particle)

    # Handle interactions
    handle_interactions()

    # Calculate energy and temperature
    current_energy = sum(zero_point_energy(PARTICLES[p]["mass"]) * count for p, count in particle_counts.items())
    total_energy += current_energy
    if len(particle_counts) > 0:
        temperature = current_energy / (len(particle_counts) * k_b * VOLUME)

    # Entropy based on particle count
    entropy += k_b * len(particle_counts) * adjusted_timestep

    # Expand volume in Big Bang mode
    if MODE == "Big Bang":
        VOLUME += 0.1 * adjusted_timestep

    time_steps += adjusted_timestep


def display_simulation(stdscr):
    """Display the simulation."""
    global VOLUME, MODE, time_delay, timestep_multiplier, total_particles_created

    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        adjusted_timestep = timestep_multiplier * time_delay

        stdscr.clear()

        # Update the simulation
        simulate_vacuum_energy(adjusted_timestep)

        # Display data
        stdscr.addstr(0, 0, f"Mode: {MODE}")
        stdscr.addstr(1, 0, f"Elapsed Earth Time: {elapsed_time:.2f}s | Simulation Timesteps: {int(time_steps)}")
        stdscr.addstr(2, 0, f"Timestep Multiplier: {timestep_multiplier}x | Effective Timestep: {adjusted_timestep:.2e}s")
        stdscr.addstr(3, 0, f"Total Particles: {total_particles_created}")
        stdscr.addstr(4, 0, f"Decayed Naturally: {total_particles_decayed_natural} | Decayed via Interaction: {total_particles_decayed_interaction}")
        avg_appearance_time = elapsed_time / total_particles_created if total_particles_created > 0 else 0
        stdscr.addstr(5, 0, f"Average Appearance Time: {avg_appearance_time:.2f}s")
        stdscr.addstr(6, 0, f"Volume: {VOLUME:.2f} m³ | Temperature: {temperature:.2f} K | Entropy: {entropy:.2f}")
        stdscr.addstr(7, 0, f"Radiation Density: {radiation_density():.2e} GeV/m³")
        stdscr.addstr(8, 0, f"Gravitational Potential: {gravitational_potential():.2e} J")

        # Display particle counts
        row = 10
        stdscr.addstr(row, 0, f"{'Particle':<15} | {'Count':<10}")
        row += 1
        stdscr.addstr(row, 0, "-" * 30)
        row += 1
        for particle, count in particle_counts.items():
            stdscr.addstr(row, 0, f"{particle:<15} | {count:<10}")
            row += 1

        # Controls
        stdscr.addstr(row + 2, 0, "Controls: [M] Toggle Mode  [R] Reset  [+/-] Adjust Timestep  [UP/DOWN/LEFT/RIGHT] Adjust Volume  [Q] Quit")

        stdscr.refresh()

        # Handle input
        stdscr.nodelay(True)
        try:
            key = stdscr.getkey()
            if key.lower() == "m":
                MODE = "Big Bang" if MODE == "Default" else "Default"
                reset_simulation()
            elif key.lower() == "r":
                reset_simulation()
            elif key == "+":
                timestep_multiplier = min(timestep_multiplier * 10, 1e9)
            elif key == "-":
                timestep_multiplier = max(timestep_multiplier / 10, 1)
            elif key == "KEY_UP":
                VOLUME += 1
            elif key == "KEY_DOWN" and VOLUME > 1:
                VOLUME -= 1
            elif key == "KEY_RIGHT":
                time_delay = max(0.01, time_delay - 0.01)
            elif key == "KEY_LEFT":
                time_delay += 0.01
            elif key.lower() == "q":
                break
        except Exception:
            pass

        time.sleep(time_delay)


def reset_simulation():
    """Reset the simulation."""
    global VOLUME, total_energy, temperature, entropy, time_steps, particle_counts, total_particles_created, total_particles_decayed_natural, total_particles_decayed_interaction
    VOLUME = 1 if MODE == "Default" else 0.1
    total_energy = 0.0
    temperature = 2.7 if MODE == "Default" else 1e12
    entropy = 0.0
    time_steps = 0
    particle_counts.clear()
    total_particles_created = 0
    total_particles_decayed_natural = 0
    total_particles_decayed_interaction = 0


def main(stdscr):
    curses.curs_set(0)
    display_simulation(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)
