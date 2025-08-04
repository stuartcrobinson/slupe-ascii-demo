=== SLUPE RESULTS ===
📋 Output copied to clipboard @ 10:12:00.808 pm
---------------------
m4q ✅ file_replace_text /Users/stuart/repos/slupe-ascii-demo/src/artist.py
=== END ===
```sh nesl
#!nesl [@three-char-SHA-256: m4q]
action = "file_replace_text"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
old_text = <<'EOT_m4q'
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
EOT_m4q
new_text = <<'EOT_m4q'
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
EOT_m4q
#!end_m4q
```