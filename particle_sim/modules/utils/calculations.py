import random
import numpy as np
from modules.constants import *
from modules.dictionaries.particles import PARTICLES
from modules.dictionaries.decay_channels import DECAY_CHANNELS
from modules.dictionaries.interaction_channels import INTERACTION_CHANNELS


def hubble_expansion(volume, adjusted_timestep):
    H = H0 * 1e3 / (3.086e22)
    return volume * (1 + H * adjusted_timestep)

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
    return total_particles_decayed_natural


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
    return total_particles_decayed_interaction


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
    global total_energy, entropy, temperature, time_steps, total_particles_created, total_particles_decayed_interaction, total_particles_decayed_natural, VOLUME, particle_counts

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
                total_particles_decayed_natural = decay_particle(particle)

    # Handle interactions
    total_particles_decayed_interaction = handle_interactions()

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

    return entropy, temperature, total_energy, total_particles_created, total_particles_decayed_interaction, total_particles_decayed_natural, particle_counts, VOLUME, timestep_multiplier, time_steps
