=== SLUPE RESULTS ===
📋 Output copied to clipboard @ 10:09:47.964 pm
---------------------
v3m ❌ file_replace_text /Users/stuart/repos/slupe-ascii-demo/src/artist.py - old_text not found in file
r8k ✅ file_read /Users/stuart/repos/slupe-ascii-demo/src/artist.py
=== END ===
```sh nesl
#!nesl [@three-char-SHA-256: v3m]
action = "file_replace_text"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
old_text = <<'EOT_v3m'
def draw_robot(frame=0):
EOT_v3m
new_text = <<'EOT_v3m'
def draw_robot(frame=0):
EOT_v3m
#!end_v3m
```

Let me read the file to see what's happening:

```sh nesl
#!nesl [@three-char-SHA-256: r8k]
action = "file_read"
path = "/Users/stuart/repos/slupe-ascii-demo/src/artist.py"
#!end_r8k
```