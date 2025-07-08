from rich.table import Table
from rich.console import Console
from vlc import MediaPlayer
console = Console()
def displayResultsTable(res: list) -> None:
    table = Table(title="🎧 Search Results", show_lines=True)
    table.add_column("ID", justify="right", style="green")
    table.add_column("Title", justify="center", style="blue")
    table.add_column("Duration", justify="center", style="red")
    table.add_column("Link", justify="center", style="yellow")
    for video in res:
        table.add_row(str(video['id']+1), video['title'], video['duration'], video['link'])
    console.print(table)

def playBackControls(player: MediaPlayer) -> None:
    while True:
        choice = input("(p)ause | (r)esume | (s)top\n> ").strip().lower()
        if choice == "p":
            player.pause()
        elif choice == "r":
            player.play()
        elif choice == "s":
            player.stop()
            break
    