import os
import shutil

# Nee Downloads path ikkada pettu
source_folder = "C:/Users/satya/Downloads"

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".log"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi", ".msix"],
    "Archives": [".zip", ".rar", ".7z"]
}

print(f"Organizing folder: {source_folder}")
print(f"Total files found: {len(os.listdir(source_folder))}")

for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

file_count = 0
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file)
        moved = False
        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                destination = os.path.join(source_folder, folder, file)
                shutil.move(file_path, destination)
                print(f"Moved: {file} → {folder}")
                moved = True
                file_count += 1
                break
        if not moved:
            others_folder = os.path.join(source_folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved: {file} → Others")
            file_count += 1

print(f"\nFile organization completed! Total {file_count} files organized.")