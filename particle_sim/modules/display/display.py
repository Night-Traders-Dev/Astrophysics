import time
import sys
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
    global total_energy, entropy, temperature, time_steps, timestep_multiplier, time_delay
    global total_particles_created, total_particles_decayed_interaction, total_particles_decayed_natural
    global particle_counts, total_particle_count, VOLUME, MODE, total_particle_counts

    # Initialize timer and counters
    start_time = time.time()
    last_update_time = start_time
    total_particles_created_last = total_particles_created
    total_particles_decayed_natural_last = total_particles_decayed_natural
    total_particles_decayed_interaction_last = total_particles_decayed_interaction

    particles_created_per_second = 0
    decayed_natural_per_second = 0
    decayed_interaction_per_second = 0

    while True:
        # Get terminal dimensions
        height, width = stdscr.getmaxyx()

        # Clear screen
        stdscr.clear()

        # Check if terminal is large enough
        if height < 15 or width < 80:
            stdscr.addstr(0, 0, "Terminal too small. Please resize to at least 80x15.")
            stdscr.refresh()
            time.sleep(1)
            continue

        # Calculate elapsed time and adjusted timestep
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_since_last_update = current_time - last_update_time
        adjusted_timestep = timestep_multiplier * time_delay

        # Update simulation
        (entropy, temperature, total_energy, total_particles_created,
         total_particles_decayed_interaction, total_particles_decayed_natural,
         particle_counts, VOLUME, timestep_multiplier, time_steps, total_particle_count, total_particle_counts) = simulate_vacuum_energy(adjusted_timestep)

        # Update total_particle_counts with new particles
        for particle, count in particle_counts.items():
            if particle not in total_particle_counts:
                total_particle_counts[particle] = count
            else:
                total_particle_counts[particle] += count

        # Update per-second rates if enough time has passed
        if time_since_last_update >= 1:  # Update rates every second
            particles_created_per_second = (total_particles_created - total_particles_created_last) / time_since_last_update
            decayed_natural_per_second = (total_particles_decayed_natural - total_particles_decayed_natural_last) / time_since_last_update
            decayed_interaction_per_second = (total_particles_decayed_interaction - total_particles_decayed_interaction_last) / time_since_last_update

            # Update tracking variables
            total_particles_created_last = total_particles_created
            total_particles_decayed_natural_last = total_particles_decayed_natural
            total_particles_decayed_interaction_last = total_particles_decayed_interaction
            last_update_time = current_time

        # Display simulation data
        stdscr.addstr(0, 0, f"Mode: {MODE}")
        stdscr.addstr(1, 0, f"Elapsed Earth Time: {elapsed_time:.2f}s | Simulation Timesteps: {time_steps:.2f}")
        stdscr.addstr(2, 0, f"Timestep Multiplier: {timestep_multiplier}x | Effective Timestep: {adjusted_timestep:.2e}s")
        stdscr.addstr(3, 0, f"Total Particles: {total_particles_created:,} | Rate: {particles_created_per_second:.2f} particles/s")
        stdscr.addstr(4, 0, f"Decayed Naturally: {total_particles_decayed_natural:,} | Rate: {decayed_natural_per_second:.2f} decays/s")
        stdscr.addstr(5, 0, f"Decayed via Interaction: {total_particles_decayed_interaction:,} | Rate: {decayed_interaction_per_second:.2f} decays/s")
        avg_appearance_time = elapsed_time / total_particles_created if total_particles_created > 0 else 0
        stdscr.addstr(6, 0, f"Average Appearance Time: {avg_appearance_time:.2f}s")
        stdscr.addstr(7, 0, f"Volume: {VOLUME:.2f} m³ | Temperature: {temperature:.2f} K | Entropy: {entropy:.2f}")
        stdscr.addstr(8, 0, f"Radiation Density: {radiation_density():.2e} GeV/m³")
        stdscr.addstr(9, 0, f"Gravitational Potential: {gravitational_potential():.2e} J")

        # Display particle counts
        row = 11
        stdscr.addstr(row, 0, f"{'Particle':<15} | {'Current Count':<15} | {'Total Count':<15} | {'Percentage':<12} | {'New Avg':<10}")
        row += 1
        stdscr.addstr(row, 0, "-" * 85)
        row += 1
        total_particles_overall = sum(total_particle_counts.values())
        for particle, count in particle_counts.items():
            if row < height - 2:
                total_count = total_particle_counts.get(particle, 0)
                percentage = (count / total_particles_created) * 100 if total_particles_created > 0 else 0
                new_avg = total_count / total_particles_overall if total_particles_overall > 0 else 0
                stdscr.addstr(row, 0, f"{particle:<15} | {count:<15,} | {total_count:<15,} | {percentage:.2f}%     | {new_avg:.2f}")
                row += 1
            else:
                break

        # Display controls
        row += 2
        if row < height:
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
                sys.exit()
        except Exception:
            pass

        time.sleep(time_delay)
