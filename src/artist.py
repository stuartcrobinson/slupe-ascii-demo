# /Users/stuart/repos/slupe-ascii-demo/src/artist.py
import time
import os
from colorama import init, Fore, Style
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_robot():
    lines = []
    lines.append(f"  {Fore.YELLOW}[{Fore.GREEN}o_o{Fore.YELLOW}]")
    lines.append(f"  {Fore.BLUE}<| |>")
    lines.append(f"   {Fore.RED}/ \\")
    return "\n".join(lines)

def main():
    clear_screen()
    print(Fore.CYAN + "Slupe Demo")
    print(draw_robot())
    
    # Keep running so we can see the output
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRobot signing off!")

if __name__ == "__main__":
    main()