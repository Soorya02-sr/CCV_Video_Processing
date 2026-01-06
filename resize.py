import cv2
import os

def resize_videos_in_folder(input_folder, output_folder, width=512, height=640):
    os.makedirs(output_folder, exist_ok=True)

    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    for video_name in video_files:
        input_path = os.path.join(input_folder, video_name)
        output_path = os.path.join(output_folder, video_name)

        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            print(f"⚠️ Skipping {video_name} (cannot open)")
            continue

        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        print(f" Resizing {video_name} → {width}×{height}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            out.write(resized)

        cap.release()
        out.release()

    print(f"✅ All resized videos saved to: {output_folder}")


# Example usage
input_folder = input("enter input path")
output_folder = input("enter the output path")
resize_videos_in_folder(input_folder, output_folder)
