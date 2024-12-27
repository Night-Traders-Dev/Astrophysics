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
    "Electron Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Muon": {"mass": 0.105, "charge": -1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Anti-Muon": {"mass": 0.105, "charge": +1, "spin": 0.5, "lifetime": 2.2e-6, "type": "fermion"},
    "Muon Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Tau": {"mass": 1.777, "charge": -1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
    "Anti-Tau": {"mass": 1.777, "charge": +1, "spin": 0.5, "lifetime": 2.9e-13, "type": "fermion"},
    "Tau Neutrino": {"mass": 1e-9, "charge": 0, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Photon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e30, "type": "boson"},
    "Neutron": {"mass": 0.939, "charge": 0, "spin": 0.5, "lifetime": 880.2, "type": "fermion"},
    "Proton": {"mass": 0.938, "charge": +1, "spin": 0.5, "lifetime": 1e30, "type": "fermion"},
    "Gluon": {"mass": 0.0, "charge": 0, "spin": 1, "lifetime": 1e-23, "type": "boson"},
    "W Boson": {"mass": 80.379, "charge": +1, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Z Boson": {"mass": 91.1876, "charge": 0, "spin": 1, "lifetime": 3e-25, "type": "boson"},
    "Higgs Boson": {"mass": 125.1, "charge": 0, "spin": 0, "lifetime": 1.56e-22, "type": "boson"},
}

# Particle Decay Channels (Branching Ratios)
DECAY_CHANNELS = {
    "Neutron": [("Proton", "Electron", "Electron Neutrino")],
    "Muon": [("Electron", "Muon Neutrino", "Electron Neutrino")],
    "Tau": [("Muon", "Muon Neutrino", "Tau Neutrino"), ("Electron", "Electron Neutrino", "Tau Neutrino")],
    "W Boson": [("Electron", "Electron Neutrino"), ("Muon", "Muon Neutrino"), ("Tau", "Tau Neutrino")],
    "Z Boson": [("Electron", "Positron"), ("Muon", "Anti-Muon")],
}

# Simulation Space
VOLUME = 1  # Initial volume in cubic meters
particle_counts = defaultdict(int)
total_energy = 0.0
total_momentum = 0.0
temperature = 2.7  # Approximation to the CMB temperature (Kelvin)
entropy = 0.0
time_steps = 0
time_delay = 0.1  # Time step duration (seconds)

def zero_point_energy(mass):
    """Calculate zero-point energy for a particle."""
    omega = c * np.sqrt(mass)
    return 0.5 * hbar * omega

def decay_particle(particle):
    """Handle particle decay using branching ratios."""
    if particle in DECAY_CHANNELS:
        decay_products = random.choice(DECAY_CHANNELS[particle])
        particle_counts[particle] -= 1
        for product in decay_products:
            particle_counts[product] += 1

def simulate_vacuum_energy():
    """Simulates particle interactions in the vacuum."""
    global total_energy, total_momentum, entropy, temperature, time_steps

    # Particle creation/annihilation
    particle_type = random.choice(list(PARTICLES.keys()))
    action = random.choice(["create", "annihilate"])
    if action == "create":
        particle_counts[particle_type] += 1
    elif action == "annihilate" and particle_counts[particle_type] > 0:
        particle_counts[particle_type] -= 1
        # Produce photons during annihilation
        if particle_type in ["Electron", "Positron", "Muon", "Anti-Muon"]:
            particle_counts["Photon"] += 2

    # Handle decays
    for particle, count in list(particle_counts.items()):
        if count > 0 and PARTICLES[particle]["lifetime"] < 1e30:  # Decay only for unstable particles
            if random.random() < 1 / PARTICLES[particle]["lifetime"]:
                decay_particle(particle)

    # Compute energy and momentum
    current_energy = sum(zero_point_energy(PARTICLES[p]["mass"]) * count for p, count in particle_counts.items() if p in PARTICLES)
    current_momentum = sum(PARTICLES[p]["mass"] * c * count for p, count in particle_counts.items() if p in PARTICLES)
    total_energy += current_energy
    total_momentum += current_momentum

    # Update temperature and entropy
    temperature = current_energy / (len(particle_counts) * k_b) if particle_counts else temperature
    entropy += k_b * len(particle_counts)

    time_steps += 1
    return current_energy / VOLUME  # Energy density

def display_vacuum_simulation(stdscr):
    """Displays the vacuum simulation using curses."""
    global VOLUME, time_delay

    time_step = 0
    while True:
        stdscr.clear()
        current_energy = simulate_vacuum_energy()
        stdscr.addstr(0, 0, f"Time Step: {time_step}")
        stdscr.addstr(1, 0, f"Volume: {VOLUME} m^3")
        stdscr.addstr(2, 0, f"Current Vacuum Energy Density: {current_energy:.6e} GeV/m^3")
        stdscr.addstr(3, 0, f"Temperature: {temperature:.6e} K")
        stdscr.addstr(4, 0, f"Entropy: {entropy:.6e} GeV/K")
        stdscr.addstr(5, 0, f"Total Momentum: {total_momentum:.6e} kg*m/s")
        stdscr.addstr(7, 0, f"{'Particle':<15} | {'Count':<10} | {'Energy (GeV)':<15}")
        stdscr.addstr(8, 0, "-" * 50)
        row = 9
        for particle, count in particle_counts.items():
            if particle in PARTICLES:
                energy = zero_point_energy(PARTICLES[particle]["mass"]) * count
                stdscr.addstr(row, 0, f"{particle:<15} | {count:<10} | {energy:<15.6e}")
                row += 1

        stdscr.addstr(row + 2, 0, "Controls: [UP] Increase Volume  [DOWN] Decrease Volume")
        stdscr.addstr(row + 3, 0, "          [LEFT] Slow Down  [RIGHT] Speed Up  [Q] Quit")
        
        stdscr.refresh()

        # Handle input
        stdscr.nodelay(True)
        try:
            key = stdscr.getkey()
            if key == "KEY_UP":
                VOLUME += 1
            elif key == "KEY_DOWN" and VOLUME > 1:
                VOLUME -= 1
            elif key == "KEY_RIGHT":
                time_delay = max(0.01, time_delay - 0.01)  # Speed up
            elif key == "KEY_LEFT":
                time_delay += 0.01  # Slow down
            elif key.lower() == "q":
                break
        except Exception:
            pass  # No input received

        time.sleep(time_delay)
        time_step += 1

def main(stdscr):
    curses.curs_set(0)
    display_vacuum_simulation(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
