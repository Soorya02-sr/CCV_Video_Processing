from moviepy.editor import VideoFileClip  # pip install moviepy
import os

# Ask for input/output folders
input_folder = input("Enter the folder path containing videos: ").strip()
output_folder = input("Enter the folder path to save processed videos: ").strip()

# Crop values
top_crop = int(input("Pixels to crop from TOP: ").strip())       # 500
bottom_crop = int(input("Pixels to crop from BOTTOM: ").strip()) # 0
left_crop = int(input("Pixels to crop from LEFT: ").strip())     # 0
right_crop = int(input("Pixels to crop from RIGHT: ").strip())   # 0

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Supported formats
video_extensions = (".mp4", ".avi", ".mov", ".mkv")

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(video_extensions):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.mp4")

        print(f"Processing: {file_name}...")

        clip = VideoFileClip(input_path)

        # Crop
        original_width, original_height = clip.size
        x1, y1 = left_crop, top_crop
        x2, y2 = original_width - right_crop, original_height - bottom_crop
        cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

        # Save with default quality settings
        cropped_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

print("✅ All videos cropped and saved successfully!")
