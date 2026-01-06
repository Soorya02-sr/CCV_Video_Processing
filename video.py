import os
from moviepy.editor import ImageSequenceClip

image_folder = 'frames' # Replace with the path to your image folder
output_video_file = 'final_video.mp4'
fps = 24 # Frames per second

image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
image_files.sort()

clip = ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(output_video_file)
print(f"Video '{output_video_file}' created successfully.")
