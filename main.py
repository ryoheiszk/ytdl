import json
from datetime import date

import yt_dlp


urls = json.load(open("target.json"))
today = date.today().strftime("%Y%m%d")


with yt_dlp.YoutubeDL({
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "merge_output_format": "mp4",
    "outtmpl": f"downloads/{today}_%(title)s.%(ext)s",
    "restrictfilenames": True,
    "ignoreerrors": True,
    "retries": 10,
    "fragment_retries": 10,
    "concurrent_fragment_downloads": 1,
    "cookiefile": "cookies.txt",
}) as ydl:
    ydl.download(urls)
