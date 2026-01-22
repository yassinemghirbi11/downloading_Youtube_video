from pytube import YouTube

url = input("Enter YouTube video URL: ")

# fix short URLs and remove extra params
if "youtu.be" in url:
    video_id = url.split("/")[-1].split("?")[0]
    url = f"https://www.youtube.com/watch?v={video_id}"
else:
    url = url.split("?")[0]  # remove any extra params

try:
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4") \
                       .order_by("resolution").desc().first()
    if stream:
        stream.download(output_path="downloads")
        print("Download complete!")
    else:
        print("No suitable stream found.")
except Exception as e:
    print("Error:", e)
