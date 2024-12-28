import time
from modules.constants import *
from modules.utils.calculations import *

def reset_simulation():
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

def display_simulation(stdscr):
    """Main display function for the simulation."""
    global total_energy, entropy, temperature, time_steps, timestep_multiplier, time_delay, total_particles_created, total_particles_decayed_interaction, total_particles_decayed_natural, particle_counts, VOLUME, MODE
    # Initialize timer
    start_time = time.time()

    while True:
        # Calculate elapsed time and adjusted timestep
        elapsed_time = time.time() - start_time
        adjusted_timestep = timestep_multiplier * time_delay

        # Update simulation
        entropy, temperature, total_energy, total_particles_created, total_particles_decayed_interaction, total_particles_decayed_natural, particle_counts, VOLUME, timestep_multiplier, time_steps = simulate_vacuum_energy(adjusted_timestep)

        # Clear screen
        stdscr.clear()

        # Display simulation data
        stdscr.addstr(0, 0, f"Mode: {MODE}")
        stdscr.addstr(1, 0, f"Elapsed Earth Time: {elapsed_time:.2f}s | Simulation Timesteps: {time_steps}")
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

        # Display controls
        row += 2
        stdscr.addstr(row, 0, "Controls: [M] Toggle Mode  [R] Reset  [+/-] Adjust Timestep  [UP/DOWN/LEFT/RIGHT] Adjust Volume  [Q] Quit")

        # Refresh display
        stdscr.refresh()

        # Handle input
        stdscr.nodelay(True)
        try:
            key = stdscr.getkey()
            if key.lower() == "m":
                MODE = "Big Bang" if MODE == "Default" else "Default"
                elapsed_time = 0
                reset_simulation()
            elif key.lower() == "r":
                elapsed_time = 0
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
