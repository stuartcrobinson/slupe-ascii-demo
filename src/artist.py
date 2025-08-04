#!/usr/bin/env python3
"""
ASCII Robot Artist - Initial static version
This file will be modified by the LLM to add animations
"""
import time
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_robot():
    """Draw a simple ASCII robot"""
    robot = """
  [o_o]
  <| |>
   / \\
    """
    robot2 = """
       ___
      |o o|
      |_-_|
     /|[ ]|\\
    d |   | b
      |   |
      |___|
      d   b
    """
    return robot

def main():
    clear_screen()
    print(Fore.CYAN + "Slupe Demo")
    print(Fore.WHITE + draw_robot())
    
    # Keep running so we can see the output
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRobot signing off!")

if __name__ == "__main__":
    main()