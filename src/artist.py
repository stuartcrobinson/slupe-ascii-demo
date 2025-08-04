import time
import os
from colorama import init, Fore, Back, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_robot():
    robot = """
           ◇◆◇
          ◆◇◆◇◆
           ◇◆◇
         
  [o_o]
  <| |>
   / \\
    """
    return robot

def colorize_line(line, color_map=None):
    if not color_map:
        return line
    
    colored_line = ""
    for char in line:
        color = color_map.get(char, "")
        colored_line += color + char
    return colored_line + Style.RESET_ALL

def render_art(art_text, line_colors=None):
    lines = art_text.strip('\n').split('\n')
    
    if line_colors:
        for i, line in enumerate(lines):
            if i < len(line_colors):
                print(line_colors[i] + line + Style.RESET_ALL)
            else:
                print(line)
    else:
        for line in lines:
            print(line)

def main():
    frame = 0
    try:
        while True:
            clear_screen()
            print(Fore.CYAN + "Slupe Demo" + Style.RESET_ALL)
            print()
            
            robot = draw_robot(frame)
            render_art(robot, [Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.YELLOW, Fore.BLUE, Fore.RED])
            
            frame += 1
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nRobot signing off!")

if __name__ == "__main__":
    main()