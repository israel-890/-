import pytube
import os


def download_audio(video):
    # stream = video.streams.filter(only_audio=True).first()
    stream = video.streams.filter(type="audio").first()
    filename = f"{input('שמור בשם:')}.mp3"
    your_downloads = os.path.expanduser("~/Downloads")
    stream.download("your_downloads", filename)


def download_video(video):
    stream = video.streams.filter(res="720p").first()
    filename = f"{input('שמור בשם:')}.mp4"
    your_downloads = os.path.expanduser("~/Downloads")
    stream.download("your_downloads", filename)


def chose_con(chose):
    if chose == 1:
        download_audio(video)
    elif chose == 2:
        download_video(video)


url = input("please enter the url: ")
video = pytube.YouTube(url)

chose = int(input("enter 1 for download audio, or 2 to download video: "))
chose_con(chose)
