import os
from moviepy.editor import VideoFileClip

src = input("Enter source folder: ").strip()
dst = input("Enter destination folder: ").strip()
os.makedirs(dst, exist_ok=True)

for file in os.listdir(src):
    if file.lower().endswith(".mpg"):
        in_path = os.path.join(src, file)
        out_name = os.path.splitext(file)[0] + ".mp4"
        out_path = os.path.join(dst, out_name)

        clip = VideoFileClip(in_path)
        clip.write_videofile(out_path, codec="libx264", audio_codec="aac")
        clip.close()

        print(f"✔ Converted: {file} → {out_name}")

print("✅ All MPG files converted to MP4!")
