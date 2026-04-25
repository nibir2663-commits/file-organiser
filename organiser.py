import os
import shutil

folder_to_organise = r"C:\Users\MC\Desktop\TestFolder"

file_groups = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv"],
    "Documents":  [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Music":      [".mp3", ".wav", ".aac"],
    "Archives":   [".zip", ".rar", ".7z"],
}

for filename in os.listdir(folder_to_organise):
    file_path = os.path.join(folder_to_organise, filename)
    if os.path.isdir(file_path):
        continue
    file_extension = os.path.splitext(filename)[1].lower()
    destination_folder = "Others"
    for group_name, extensions in file_groups.items():
        if file_extension in extensions:
            destination_folder = group_name
            break
    destination_path = os.path.join(folder_to_organise, destination_folder)
    os.makedirs(destination_path, exist_ok=True)
    shutil.move(file_path, os.path.join(destination_path, filename))
    print(f"Moved: {filename}  →  {destination_folder}/")

print("\nDone! Your folder is now organised.")