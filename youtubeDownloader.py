from pytube import YouTube
from sys import argv

link = "https://www.youtube.com/watch?v=QD6Zp_gXYDU"
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('./youtubeVideos')