import json

from youtube_dl import YoutubeDL


def main(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        ytdl_data = json.load(f)

    for course in ytdl_data:
        ydl_opts = {
        "outtmpl": "./yt_videos/{}/%(title)s.%(ext)s".format(course["name"]),
        "recodevideo": "mp4"
        }
        ydl = YoutubeDL(ydl_opts)

        ydl.download(course["videos"])

if __name__ == "__main__":
    main("ytdl_data.json")

    import subprocess
    subprocess.call('PAUSE', shell=True)
