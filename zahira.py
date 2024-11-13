 from pytube import YouTube
link = input("url :")
video = YouTube(link)
stream = video.get_highest_resolution()
stream.download()
