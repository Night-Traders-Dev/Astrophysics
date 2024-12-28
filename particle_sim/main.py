import curses
from modules.display.display import display_simulation

def main(stdscr):
    curses.curs_set(0)
    while True:
        display_simulation(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
