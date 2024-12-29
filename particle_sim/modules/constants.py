from collections import defaultdict

# Universal Constants
c = 3e8  # Speed of light in vacuum (m/s)
hbar = 6.582119569e-25  # Reduced Planck constant (GeV*s)
k_b = 8.617333262145e-5  # Boltzmann constant (GeV/K)
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
H0 = 67.4  # Hubble's constant (km/s/Mpc)
dark_energy_density = 7.3e-30  # Dark energy density (kg/m^3)

# Derived Constants
H0_in_s = H0 * 1e3 / (3.086e22)  # Hubble's constant converted to 1/s

# Simulation Variables
MODE = "Default"
VOLUME = 1.0
particle_counts = defaultdict(int)
total_particle_counts = defaultdict(int)
total_energy = 0.0
temperature = 1e12
entropy = 0.0
time_steps = 0
time_delay = 0.1
timestep_multiplier = 1
total_particle_count = 0
total_particles_created = 0
total_particles_decayed_natural = 0
total_particles_decayed_interaction = 0
