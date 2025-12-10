import os
import subprocess
import re


# 🔧 HARD-CODED PATHS (Change these)
VIDEO_PATH = r"Mission.Impossible.II.2000.1080p.BluRay.x264-[YTS.AG].mp4"
SUBTITLE_PATH = r"Mission.Impossible.II.2000-en.srt"
OUTPUT_DIR = r"C:\Users\chait\Desktop\Mission Impossible II (2000) [1080p] [YTS.AG]"


def get_video_duration(video_path):
    """Return the video duration in seconds."""
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                video_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except Exception as e:
        print("❌ Error getting video duration:", e)
        return None


def burn_subtitles_with_progress(video_path, subtitle_path, output_dir):
    if not os.path.isfile(video_path):
        print(f"❌ Video file not found: {video_path}")
        return
    if not os.path.isfile(subtitle_path):
        print(f"❌ Subtitle file not found: {subtitle_path}")
        return
    if not os.path.isdir(output_dir):
        print(f"❌ Output directory not found: {output_dir}")
        return

    duration = get_video_duration(video_path)
    if not duration:
        print("❌ Could not determine video duration.")
        return

    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{video_filename}_burned.mp4")
    escaped_sub_path = subtitle_path.replace("\\", "\\\\")

    print("\n🚀 Burning subtitles into video...\n")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"subtitles='{escaped_sub_path}'",
        "-y",  # Overwrite output
        output_path
    ]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )

    time_pattern = re.compile(r"time=(\d+:\d+:\d+\.\d+)")

    def time_str_to_seconds(timestr):
        h, m, s = timestr.split(":")
        return int(h) * 3600 + int(m) * 60 + float(s)

    try:
        for line in process.stdout:
            match = time_pattern.search(line)
            if match:
                current_time = time_str_to_seconds(match.group(1))
                percent = (current_time / duration) * 100
                print(f"\r⏳ Progress: {percent:.2f}%", end="", flush=True)
        process.wait()
        if process.returncode == 0:
            print(f"\n✅ Done! Output saved to: {output_path}")
        else:
            print("\n❌ FFmpeg failed.")
    except Exception as e:
        print("\n❌ Error running FFmpeg:", e)


if __name__ == "__main__":
    burn_subtitles_with_progress(VIDEO_PATH, SUBTITLE_PATH, OUTPUT_DIR)
