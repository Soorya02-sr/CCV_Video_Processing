import os
import re

# Folder path containing files
folder_path = input("Enter folder path: ").strip()

# Regex pattern: matches _ followed by digits at end of filename (before extension)
pattern = re.compile(r"_(\d+)(?=\.[^.]+$)|_(\d+)$")

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)
    if os.path.isfile(old_path):
        # Remove timestamp pattern
        new_name = re.sub(pattern, '', filename)
        new_path = os.path.join(folder_path, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

print("\n✅ Done! All timestamps removed.")
