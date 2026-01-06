import cv2
import os

def video_to_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_id = 0

    while True:
        ret, frame = cap.read()  #ret=return value(true or false)
        if not ret:
            break
        frame_id += 1
        if ret:
           cv2.imwrite(os.path.join(output_folder, f"frame_{frame_id:04d}.png"), frame)                  #imwrite() is to save image to file

    cap.release()
    print(f"✅ Done! {frame_id} frames saved in '{output_folder}'.")


if __name__ == "__main__":
    video_path = input("Enter path to video: ").strip()
    output_folder = input("Enter output folder for frames: ").strip()
    video_to_frames(video_path, output_folder)



