import argparse
import vlc

from search import searchForSongs
from player import playAudio
from utils import displayResultsTable, playBackControls
from rich.prompt import Prompt
from rich.console import Console
console = Console()

LIMIT = 5

parser = argparse.ArgumentParser()

parser.add_argument("--limit", type=int, default=LIMIT, help="Number of videos to search")
parser.add_argument("--query", type=str, default="Metallica", help="Search query")

args = parser.parse_args()

LIMIT = args.limit
res = searchForSongs(args.query, LIMIT)

displayResultsTable(res)

choice = Prompt.ask("Enter your choice: ", choices=[str(i+1) for i in range(LIMIT)])
choice = int(choice)
choice_url = res[choice-1]['link'] 
with console.status("⏳ Extracting stream and starting playback...", spinner="dots"):
    url = playAudio(choice_url)
console.print(f"✅ Now Playing: [bold cyan]{res[choice-1]['title']}[/]")

player = vlc.MediaPlayer(url)
player.play()

playBackControls(player)