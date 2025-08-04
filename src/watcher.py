#!/usr/bin/env python3
"""
File watcher that restarts artist.py when it changes
"""
import os
import sys
import time
import subprocess
import signal
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.text import Text

console = Console()

debug = False

class ArtistFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.artist_path = Path(__file__).parent / "artist.py"
        self.restart_count = 0
        self.start_artist()
    
    def start_artist(self):
        """Start the artist.py script"""
        self.stop_artist()


        
        debug and console.print(f"[green]{'Starting' if self.restart_count == 0 else 'Restarting'} artist.py...[/green]")
        
        try:
            # Run artist.py as a subprocess
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'
            env['FORCE_COLOR'] = '1'
            env['COLORAMA_FORCE_COLOR'] = '1'
            self.process = subprocess.Popen(
                [sys.executable, '-u', str(self.artist_path)],
                env=env,
                preexec_fn=os.setsid if os.name != 'nt' else None,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
            )
            
            # Start a thread to read output
            import threading
            self.output_thread = threading.Thread(target=self.read_output, daemon=True)
            self.output_thread.start()
            
            if self.restart_count > 0:
                debug and console.print(f"[yellow]✨ Reloaded! (Change #{self.restart_count})[/yellow]")
            self.restart_count += 1
            
        except Exception as e:
            debug and console.print(f"[red]Error starting artist.py: {e}[/red]")
    
    def read_output(self):
        """Read and display output from artist.py"""
        pass
    
    def stop_artist(self):
        """Stop the currently running artist.py"""
        if self.process:
            try:
                if os.name == 'nt':
                    self.process.send_signal(signal.CTRL_BREAK_EVENT)
                else:
                    os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
                self.process.wait(timeout=2)
            except:
                self.process.kill()
            self.process = None
    
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('artist.py'):
            debug and console.print(f"\n[cyan]🔄 Detected change in artist.py[/cyan]")
            time.sleep(0.5)  # Small delay to ensure file is fully written
            self.start_artist()

def main():
    debug and console.print(Panel.fit(
        "[bold cyan]Slupe Demo Watcher[/bold cyan]\n"
        "Watching artist.py for changes...\n"
        "Press Ctrl+C to stop",
        border_style="cyan"
    ))
    
    # Set up file watcher
    event_handler = ArtistFileHandler()
    observer = Observer()
    
    watch_path = Path(__file__).parent
    observer.schedule(event_handler, str(watch_path), recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        debug and console.print("\n[yellow]Stopping watcher...[/yellow]")
        event_handler.stop_artist()
        observer.stop()
    
    observer.join()
    debug and console.print("[green]Watcher stopped.[/green]")

if __name__ == "__main__":
    main()