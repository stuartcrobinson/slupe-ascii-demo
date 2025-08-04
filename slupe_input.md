=== SLUPE RESULTS ===
📋 Output copied to clipboard @ 10:04:42.883 pm
---------------------
n7q ✅ file_replace_text /Users/stuart/repos/slupe-ascii-demo/src/artist.py
x2m ✅ file_replace_text /Users/stuart/repos/slupe-ascii-demo/src/artist.py
=== END ===
```sh nesl
#!nesl [@three-char-SHA-256: n7q]
action = "file_replace_text"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
old_text = <<'EOT_n7q'
def draw_robot():
    robot = """
  [o_o]
  <| |>
   / \\
    """
    return robot
EOT_n7q
new_text = <<'EOT_n7q'
def draw_robot():
    robot = """
        ◇◆◇
       ◆◇◆◇◆
        ◇◆◇
         |
  [o_o]
  <| |>
   / \\
    """
    return robot
EOT_n7q
#!end_n7q
```

```sh nesl
#!nesl [@three-char-SHA-256: x2m]
action = "file_replace_text"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
old_text = <<'EOT_x2m'
    render_art(robot, [Fore.YELLOW, Fore.BLUE, Fore.RED])
EOT_x2m
new_text = <<'EOT_x2m'
    render_art(robot, [Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.YELLOW, Fore.BLUE, Fore.RED])
EOT_x2m
#!end_x2m
```