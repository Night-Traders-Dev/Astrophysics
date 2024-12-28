import time
import curses
from modules.utils.calculations import simulate_vacuum_energy
from modules.display.display import display_simulation

def main(stdscr):
    curses.curs_set(0)
    while True:
        display_simulation(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
