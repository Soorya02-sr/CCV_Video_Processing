#process through subfolders

import os

folder = input("Enter the main folder path: ").strip()
txt_path = os.path.join(folder, "wordlist.txt")

# Load existing file names if txt exists
existing_names = set()
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # Skip the first line (total count) and blank line
        for line in lines[2:]:
            existing_names.add(line.strip())

# Collect all file names from all subfolders
for root, _, files in os.walk(folder):
    for file in files:
        # Skip the txt file itself
        if file == "wordlist.txt":
            continue
        name, _ = os.path.splitext(file)
        existing_names.add(name.strip())

# Sort names alphabetically
all_names = sorted(existing_names)

# Write back to txt file with total count
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(f"Total files: {len(all_names)}\n\n")
    for name in all_names:
        f.write(name + "\n")

print(f"✅ Updated {txt_path} with {len(all_names)} unique files.")








    




# import os

# folder = input("Enter the main folder path: ").strip()
# txt_path = os.path.join(folder, "all_files.txt")

# # Load existing entries if file already exists
# existing = {}
# if os.path.exists(txt_path):
#     with open(txt_path, "r", encoding="utf-8") as f:
#         lines = f.readlines()
#         subfolder = None
#         for line in lines:
#             line = line.strip()
#             if not line:
#                 continue
#             if line.startswith("[") and line.endswith("]"):
#                 subfolder = line[1:-1]  # extract subfolder name
#                 existing[subfolder] = set()
#             elif subfolder:
#                 existing[subfolder].add(line)

# # Collect new file names
# new_data = {}
# total_files = 0

# for root, _, files in os.walk(folder):
#     if root == folder:
#         continue  # skip the main folder itself

#     subfolder_name = os.path.basename(root)
#     file_names = [f for f in files if os.path.isfile(os.path.join(root, f))]

#     if file_names:
#         if subfolder_name not in existing:
#             existing[subfolder_name] = set()
#         # Add only new files
#         for name in file_names:
#             existing[subfolder_name].add(name)

# # Write back the merged results
# with open(txt_path, "w", encoding="utf-8") as f:
#     all_files_count = sum(len(files) for files in existing.values())
#     f.write(f"Total files: {all_files_count}\n\n")
#     for subfolder, files in existing.items():
#         # f.write(f"[{subfolder}]\n")
#         for name in sorted(files):
#             f.write(name + "\n")
#         f.write("\n")  # blank line between subfolders

# print(f"✅ Updated file list saved to {txt_path}")