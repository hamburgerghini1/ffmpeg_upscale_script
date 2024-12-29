import os
import subprocess

# Directory containing your videos
video_dir = r"C:\Users\tommi\Videos\Anime\[Anime Time] Gintama Complete Series (001-367+Movies) [BD] [1080p][HEVC 10bit x265][AAC][Eng Sub]"

for file in os.listdir(video_dir):
    if file.endswith(".mkv"):
        input_path = os.path.join(video_dir, file)
        output_path = os.path.join(video_dir, f"{os.path.splitext(file)[0]}.mp4")
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-vf", "scale=1920:1080:flags=lanczos",
            "-c:v", "libx264", "-crf", "18", "-preset", "slow",
            "-c:a", "aac", "-b:a", "192k",
            output_path
        ])
