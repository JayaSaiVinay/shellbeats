import threading
import random
import time

from rich.table import Table
from rich.console import Console
from rich.live import Live
from rich.text import Text
from vlc import MediaPlayer

console = Console()

# Search Results Display    
def displayResultsTable(res: list) -> None:
    table = Table(title="🎧 Search Results", show_lines=True)
    table.add_column("ID", justify="right", style="green")
    table.add_column("Title", justify="center", style="blue")
    table.add_column("Duration", justify="center", style="red")
    table.add_column("Link", justify="center", style="yellow")

    for video in res:
        table.add_row(
            str(video['id'] + 1),
            video['title'],
            video['duration'],
            video['link']
        )

    console.print(table)

# Playback Controls
def playBackControls(player: MediaPlayer) -> None:
    while True:
        choice = input("\n(p)ause | (r)esume | (s)top\n> ").strip().lower()
        if choice == "p":
            player.pause()
        elif choice == "r":
            player.play()
        elif choice == "s":
            player.stop()
            break

# Audio Visualizer
stop_visualizer = threading.Event()
visualizer_thread = None

def startVisualizer(title: str) -> None:
    global visualizer_thread

    def animate():
        blocks = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        with Live(Text(), refresh_per_second=10) as live:
            while not stop_visualizer.is_set():
                row = " ".join(random.choices(blocks, k=24))
                live.update(Text(f"🎧 Now Playing: {title}\n{row}", style="bold cyan"))
                time.sleep(0.2)

    visualizer_thread = threading.Thread(target=animate, daemon=True)
    visualizer_thread.start()

def stopVisualizer() -> None:
    stop_visualizer.set()
    if visualizer_thread:
        visualizer_thread.join()
    stop_visualizer.clear()
