from pytube import YouTube

link = "https://www.youtube.com/watch?v=QD6Zp_gXYDU"
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('./youtubeVideos')
