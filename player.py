import yt_dlp 
def playAudio(url):
    stream_url = None
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'bestaudio/best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
        info = ydl.extract_info(url, download=False)
        stream_url = info['url']
    return stream_url