=== SLUPE RESULTS ===
📋 Output copied to clipboard @ 10:11:30.571 pm
---------------------
w9k ✅ file_replace_text /Users/stuart/repos/slupe-ascii-demo/src/artist.py
=== END ===
```sh nesl
#!nesl [@three-char-SHA-256: w9k]
action = "file_replace_text"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
old_text = <<'EOT_w9k'
def draw_robot(frame=0):
    frames = [
        """
        ◇◆◇
       ◆◇◆◇◆
        ◇◆◇
         |
  [o_o]
  <| |>
   / \\
    """,
        """
        ◆◇◆
       ◇◆◇◆◇
        ◆◇◆
         |
  [o_o]
  \\| |/
   / \\
    """,
        """
        ◇◆◇
       ◆◇◆◇◆
        ◇◆◇
         |
  [o_o]
  /| |\\
   / \\
    """,
        """
        ◆◇◆
       ◇◆◇◆◇
        ◆◇◆
         |
  [^_^]
  \\| |/
   \\ /
    """
    ]
    return frames[frame % len(frames)]
EOT_w9k
new_text = <<'EOT_w9k'
def draw_robot(frame=0):
    frames = [
        """
        ◇◆◇
       ◆◇◆◇◆
        ◇◆◇
         |
  [o_o]
  <| |>
   / \\
    """,
        """
           ◆◇◆
          ◇◆◇◆◇
           ◆◇◆
            |
     [o_o]
     \\| |/
      / \\
    """,
        """
        ◇◆◇
       ◆◇◆◇◆
        ◇◆◇
         |
          [o_o]
          /| |\\
           / \\
    """,
        """
     ◆◇◆
    ◇◆◇◆◇
     ◆◇◆
      |
[^_^]
\\| |/
 \\ /
    """
    ]
    return frames[frame % len(frames)]
EOT_w9k
#!end_w9k
```