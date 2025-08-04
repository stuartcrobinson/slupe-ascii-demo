import time
import os
import random
from colorama import init, Fore, Style
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_robot_pose1():
    return """
    \\[o_o]/
     <| |>
      / \\"""

def draw_robot_pose2():
    return """
     [o_o]
    -<| |>-
      / \\"""

def draw_robot_pose3():
    return """
     [^_^]
     <| |>-
     /  \\"""

def draw_robot_pose4():
    return """
     [o_o]
    /<| |>
      \\ /"""

def draw_robot_pose5():
    return """
     [*_*]
     <| |>\\
     /  \\"""

def draw_robot_pose6():
    return """
    /[o_o]\\
     <| |>
      | |"""

def draw_robot_pose7():
    return """
     [>_<]
    \\<| |>/
      ^ ^"""

def draw_robot_pose8():
    return """
     [@_@]
     <| |>
     _/ \\_"""

def draw_dino_pose1():
    return """
       __
      / o>
     /  )
    /__/\\"""

def draw_dino_pose2():
    return """
       __
      < o\\
     (  \\
    /\\__\\"""

def draw_dino_pose3():
    return """
       __
      / ^>
     /  )
    \\__/\\"""

def draw_dino_pose4():
    return """
       __
      < o\\
     \\  )
    /\\__/"""

def draw_dino_pose5():
    return """
       __
      / *>
     (  )
    /__\\\\"""

def draw_dino_pose6():
    return """
       ^^
      / o>
     /  |
    /__/\\"""

def draw_dino_pose7():
    return """
       __
      < ->
     (  )
    /\\/\\\\"""

def draw_dino_pose8():
    return """
       ~~
      / @>
     \\  )
    \\__//"""

def main():
    robot_poses = [
        draw_robot_pose1,
        draw_robot_pose2,
        draw_robot_pose3,
        draw_robot_pose4,
        draw_robot_pose5,
        draw_robot_pose6,
        draw_robot_pose7,
        draw_robot_pose8,
        draw_robot_pose7,
        draw_robot_pose6,
        draw_robot_pose5,
        draw_robot_pose4,
        draw_robot_pose3,
        draw_robot_pose2,
    ]
    
    dino_poses = [
        draw_dino_pose1,
        draw_dino_pose2,
        draw_dino_pose3,
        draw_dino_pose4,
        draw_dino_pose5,
        draw_dino_pose6,
        draw_dino_pose7,
        draw_dino_pose8,
        draw_dino_pose7,
        draw_dino_pose6,
        draw_dino_pose5,
        draw_dino_pose4,
        draw_dino_pose3,
        draw_dino_pose2,
    ]
    
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.RED]
    
    try:
        frame = 0
        while True:
            clear_screen()
            
            current_color = colors[frame % len(colors)]
            dino_color = colors[(frame + 3) % len(colors)]
            
            print(current_color + Style.BRIGHT + "✨ SLUPE & DINO DANCE PARTY ✨")
            print()
            
            robot_lines = robot_poses[frame % len(robot_poses)]().split('\n')
            dino_lines = dino_poses[frame % len(dino_poses)]().split('\n')
            
            max_lines = max(len(robot_lines), len(dino_lines))
            
            for i in range(max_lines):
                spaces = " " * (3 + int(2 * abs(frame % 6 - 3)))
                
                robot_line = robot_lines[i] if i < len(robot_lines) else "      "
                dino_line = dino_lines[i] if i < len(dino_lines) else "     "
                
                print(spaces + current_color + robot_line + "    " + dino_color + dino_line)
            
            print()
            print(" " * 8 + "♪ ♫ ♪ ♫ ♪ ♫ ♪")
            
            hearts = ["💕", "💖", "💗", "💝", "💓", "💞"]
            if frame % 4 == 0:
                print(" " * 12 + random.choice(hearts))
            
            time.sleep(0.2)
            frame += 1
            
    except KeyboardInterrupt:
        clear_screen()
        print()
        print(Fore.CYAN + "  [^_^]/    " + Fore.GREEN + "   __")
        print(Fore.CYAN + "  <| |>     " + Fore.GREEN + "  / ^>")
        print(Fore.CYAN + "   / \\      " + Fore.GREEN + " /  )")
        print(Fore.CYAN + "            " + Fore.GREEN + "/__/\\")
        print()
        print(Fore.YELLOW + "  Thanks for dancing with us!")
        print()

if __name__ == "__main__":
    main()