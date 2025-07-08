from youtubesearchpython import VideosSearch 

def searchForSongs(query, limit):
    videosSearch = VideosSearch(query, limit = limit)
    res = videosSearch.result()
    results = res["result"]
    formatted = []
    for i, video in enumerate(results):
        formatted.append({
            "id": i,
            "video_id": video["id"],
            "title": video["title"],
            "duration": video["duration"],
            "link": video["link"]
        })
    return formatted