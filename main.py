import argparse
import vlc

from search import searchForSongs
from player import playAudio
LIMIT = 10

parser = argparse.ArgumentParser()

parser.add_argument("--limit", type=int, default=LIMIT, help="Number of videos to search")
parser.add_argument("--query", type=str, default="Metallica", help="Search query")

args = parser.parse_args()

LIMIT = args.limit
res = searchForSongs(args.query, LIMIT) 

for video in res:
    print(f"[{video['id']+1}] {video['title']} ({video['duration']})")
    print(f"     {video['link']}")

choice = int(input("Enter your choice: "))
choice_url = res[choice-1]['link'] 
url = playAudio(choice_url)
print(url)
player = vlc.MediaPlayer(url)
player.play()

input("🎵 Press Enter to stop playback...")
player.stop()
