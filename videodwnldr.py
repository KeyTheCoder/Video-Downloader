from pytube import YouTube

link = input("Enter The Video Link : ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print("Your video is downloaded in your desktop :D !")