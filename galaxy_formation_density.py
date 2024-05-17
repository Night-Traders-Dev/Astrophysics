import numpy as np
import curses
import time

# Constants
H_0 = 70  # Hubble constant (km/s/Mpc)
rho_crit_0 = 1e-29  # Critical density of the universe at present (kg/m^3)
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
cosmic_inflation_factor = 1e26  # Approximate factor by which the universe expanded during inflation
overall_mass_limit = 1e12  # Overall mass limit for galaxy formation (kg)
star_death_rate = 0.01  # Fraction of stellar mass that dies each time step
black_hole_formation_rate = 0.001  # Fraction of stellar mass that turns into black holes each time step
gas_accretion_rate = 0.05  # Fraction of gas accreted onto the galaxy each time step
gas_ejection_rate = 0.02  # Fraction of gas ejected from the galaxy each time step
supernova_feedback_rate = 0.001  # Fraction of gas ejected due to supernova feedback each time step
dark_matter_halo_growth_rate = 0.03  # Growth rate of the dark matter halo

# Simulated data for galaxy formation and mass density
def simulate_galaxy_formation_and_density(time_step, inflation_factor, total_mass, stellar_mass, black_hole_mass, gas_mass, dark_matter_mass, star_formation_rate):
    t = time_step / 1000  # Normalize time for each step
    inflation = 1 + inflation_factor * t**2  # Simplified model for cosmic inflation

    galaxy_formation_rate = np.exp(-5 * (t - 0.5)**2)  # Peak formation rate at the middle of the timeline
    galaxy_formation_rate = min(galaxy_formation_rate, overall_mass_limit - total_mass)  # Cap by overall mass limit
    mass_density = rho_crit_0 / inflation  # Simplified inverse relation to inflation

    # Update masses
    total_mass += galaxy_formation_rate
    stellar_mass += star_formation_rate * gas_mass  # New stars form from gas
    gas_mass += gas_accretion_rate * gas_mass - gas_ejection_rate * gas_mass - supernova_feedback_rate * gas_mass
    stellar_mass -= star_death_rate * stellar_mass  # Apply star death rate
    black_hole_mass += black_hole_formation_rate * stellar_mass  # Apply black hole formation rate
    dark_matter_mass += dark_matter_halo_growth_rate * dark_matter_mass  # Apply dark matter halo growth rate

    return t, inflation, galaxy_formation_rate, mass_density, total_mass, stellar_mass, black_hole_mass, gas_mass, dark_matter_mass

# Function to display data in curses
def display_galaxy_formation_and_density(stdscr):
    time_step = 0
    avg_inflation = 0
    avg_galaxy_formation_rate = 0
    avg_mass_density = 0
    total_mass = 0
    stellar_mass = 0
    black_hole_mass = 0
    gas_mass = 1e11  # Initial gas mass (kg)
    dark_matter_mass = 1e12  # Initial dark matter mass (kg)
    star_formation_rate = 0.01  # Initial star formation rate

    # Initialize curses
    curses.curs_set(0)  # Hide the cursor

    while True:
        # Simulate data
        t, inflation, galaxy_formation_rate, mass_density, total_mass, stellar_mass, black_hole_mass, gas_mass, dark_matter_mass = simulate_galaxy_formation_and_density(
            time_step, cosmic_inflation_factor, total_mass, stellar_mass, black_hole_mass, gas_mass, dark_matter_mass, star_formation_rate)

        # Update averages
        avg_inflation = (avg_inflation * time_step + inflation) / (time_step + 1)
        avg_galaxy_formation_rate = (avg_galaxy_formation_rate * time_step + galaxy_formation_rate) / (time_step + 1)
        avg_mass_density = (avg_mass_density * time_step + mass_density) / (time_step + 1)

        # Clear screen
        stdscr.clear()

        # Print headers
        stdscr.addstr(0, 0, f"Time Step: {time_step}")
        stdscr.addstr(1, 0, f"{'Time':>10} | {'Inflation Factor':>20} | {'Galaxy Formation Rate':>25} | {'Mass Density (kg/m^3)':>25}")
        stdscr.addstr(2, 0, "-" * 90)

        # Print current values
        stdscr.addstr(3, 0, f"{t:10.4f} | {inflation:20.2e} | {galaxy_formation_rate:25.2e} | {mass_density:25.2e}")

        # Print average values
        stdscr.addstr(5, 0, "Average Values:")
        stdscr.addstr(6, 0, f"{'':>10} | {avg_inflation:20.2e} | {avg_galaxy_formation_rate:25.2e} | {avg_mass_density:25.2e}")

        # Print mass information
        stdscr.addstr(8, 0, "Mass Information:")
        stdscr.addstr(9, 0, f"Total Mass: {total_mass:.2e} kg")
        stdscr.addstr(10, 0, f"Stellar Mass: {stellar_mass:.2e} kg")
        stdscr.addstr(11, 0, f"Black Hole Mass: {black_hole_mass:.2e} kg")
        stdscr.addstr(12, 0, f"Gas Mass: {gas_mass:.2e} kg")
        stdscr.addstr(13, 0, f"Dark Matter Mass: {dark_matter_mass:.2e} kg")

        # Refresh the screen
        stdscr.refresh()

        # Sleep for a short time before the next update
        time.sleep(0.1)

        # Increment time step
        time_step += 1

# Main function
def main(stdscr):
    display_galaxy_formation_and_density(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
