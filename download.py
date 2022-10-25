from pytube import YouTube
from sys import argv
try:
    link = argv[1]
    quality = argv[2]
    yt = YouTube(link)
except:
    print("Please enter a valid link")
    exit()

print("Title: ", yt.title)
print("Channel: ", yt.author)
print("Views: ", yt.views)
try:
    if quality == "720p":
        print("Downloading 720p")
        ys = yt.streams.get_highest_resolution()
        ys.download('./YTfolder')
    if quality == "480p":
        print("Downloading 480p")
        ys = yt.streams.get_by_itag(22)
        ys.download('./YTfolder')
    if quality == "360p":
        print("Downloading 360p")
        ys = yt.streams.get_by_itag(18)
        ys.download('./YTfolder')
    if quality == "240p":
        print("Downloading 240p")
        ys = yt.streams.get_by_itag(36)
        ys.download('./YTfolder')
    if quality == "144p":
         print("Downloading 144p")
         ys = yt.streams.get_by_itag(17)
         ys.download('./YTfolder')
    if quality == "audio":
        print("Downloading audio")
        ys = yt.streams.get_audio_only()
        ys.download('./YTfolder')
    if quality == "1080p":
        print("Downloading 1080p")
        ys = yt.streams.get_by_itag(137)
        ys.download('./YTfolder')
    if quality =="h":
        print("Downloading highest quality")
        ys = yt.streams.get_highest_resolution()
        ys.download('./YTfolder')
except:
    print("Ha ocurrido un error, es posible que la "
          "calidad de video no esté disponible para el video introducido")
    exit()

print("-Download completed-")