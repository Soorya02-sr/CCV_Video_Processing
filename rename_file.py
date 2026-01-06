import os, re, shutil

def clean(name):
    # name = re.sub(r"\(.*?\)", "", name)   # remove text inside ()
    name = name.replace("_", " ")         # replace _ with space
    return re.sub(r"\s+", " ", name).strip()  # remove extra spaces

src = input("Enter source folder: ").strip()
dst = input("Enter destination folder: ").strip()

os.makedirs(dst, exist_ok=True)

for root, _, files in os.walk(src):
    for f in files:
        if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv")):
            name, ext = os.path.splitext(f)
            new_name = clean(name) + ext
            shutil.copy2(os.path.join(root, f), os.path.join(dst, new_name))
            print(f"✔ {f} → {new_name}")

print("✅ Done!")







#single file renaming

# import os, re, shutil

# def clean(name):
#     # Remove underscores and extra spaces, but keep parentheses as is
#     name = name.replace("_", " ")         
#     return re.sub(r"\s+", " ", name).strip()

# src = input("Enter source folder: ").strip()
# dst = input("Enter destination folder: ").strip()

# os.makedirs(dst, exist_ok=True)

# for root, _, files in os.walk(src):
#     for f in files:
#         if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".mpg")):
#             name, ext = os.path.splitext(f)
#             new_name = clean(name) + ext

#             # Skip if new_name still has parentheses
#             if "(" in new_name or ")" in new_name:
#                 print(f"⏭ Skipped: {f} (contains parentheses after renaming)")
#                 continue  

#             shutil.copy2(os.path.join(root, f), os.path.join(dst, new_name))
#             print(f"✔ {f} → {new_name}")

# print("✅ Done!")



