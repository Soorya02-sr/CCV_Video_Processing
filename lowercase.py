import os

def rename(folder_path):
    
    video_ext = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm')

    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    print(f"Processing folder: {folder_path}")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file and has a video extension
        if os.path.isfile(file_path) and filename.lower().endswith(video_ext):
            new_filename = filename.lower()
            new_file_path = os.path.join(folder_path, new_filename)

            if filename != new_filename:  # Only rename if the name actually changes
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                except OSError as e:
                    print(f"Error renaming '{filename}': {e}")
            else:
                print(f"'{filename}' is already lowercase.")
        elif os.path.isfile(file_path):
            print(f"Skipping non-video file: '{filename}'")

target_folder = input("enter path")
rename(target_folder)




