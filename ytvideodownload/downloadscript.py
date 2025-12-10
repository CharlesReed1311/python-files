import yt_dlp
import os

def download_youtube_video(url, output_directory='.'):
    os.makedirs(output_directory, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height=1080]+bestaudio/best[height=1080]/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    output_directory = input("Enter the output directory path (leave empty for current folder): ").strip()
    if not output_directory:
        output_directory = '.'

    download_youtube_video(video_url, output_directory)
    print("✅ Download complete!")
