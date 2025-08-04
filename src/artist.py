import time
import os
from colorama import init, Fore, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(Fore.CYAN + "Slupe Demo" + Style.RESET_ALL)
    print()
    print(Fore.YELLOW + "  [" + Fore.GREEN + "o_o" + Fore.YELLOW + "]")
    print(Fore.BLUE + "  <| |>")
    print(Fore.RED + "   / \\")
    print(Style.RESET_ALL)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRobot signing off!")

if __name__ == "__main__":
    main()