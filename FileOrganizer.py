import os
import shutil
import csv

path = input("Enter path in which you want to organize files: ")
if not os.path.exists(path) or not os.path.isdir(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)
print("List of files:")
for f in files:
    print(f"  - {f}")

file_types = {
    "Word Documents": [".doc", ".docx"],
    "Excel Files": [".xls", ".xlsx", ".csv"],
    "PowerPoint Files": [".ppt", ".pptx"],
    "PDFs": [".pdf"],
    "Text Files": [".txt", ".md"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac"],
    "Video Files": [".mp4", ".mov", ".avi", ".mkv"],
    "Python Files": [".py"],
    "SQL Files": [".sql", ".parquet"],
    "Compressed Files": [".zip", ".rar", ".tar"],
}

ext_map = {}
for category, extensions in file_types.items():
    for ext in extensions:
        ext_map[ext] = category

destination = os.path.join(path, "Organized files")
if not os.path.exists(destination):
    os.mkdir(destination)

report_data = []

for file in files:
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path) or file == "Organized files" or file == "Organized files report.csv" or file=="FileOrganizer.py":
        continue
    filename, extension = os.path.splitext(file)
    ext = extension.lower()
    category = ext_map.get(ext)
    if category:
        folder_path = os.path.join(destination, category)
        os.makedirs(folder_path, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(folder_path, file))
            report_data.append([file, category, folder_path])
        except:
            print("Error moving:", file)
    else:
        print(f"{file} moved to others folder since there is a format mismatch")
        others_path = os.path.join(destination, "Others")
        os.makedirs(others_path, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(others_path, file))
            report_data.append([file, "Others", others_path])
        except:
            print("Error moving:", file)
print("Files are organized successfully!")

delete = input("Do you want to delete any file/folder? Enter its name (or 'no'): ")
if delete.lower() != 'no':
    full_path = os.path.join(path, delete)
    if os.path.exists(full_path):
        if os.path.isdir(full_path):
            if os.listdir(full_path):
                confirm = input(f"This folder '{delete}' is not empty. Delete anyway? (y/n): ")
                if confirm.lower() == 'y':
                    shutil.rmtree(full_path)
            else:
                os.rmdir(full_path)
        else:
            os.remove(full_path)
        print("Deleted successfully")
    else:
        print("File/Folder not found")

print("\nList of files in given path now:")
for item in os.listdir(path):
    print(f"  - {item}")

for folder in os.listdir(destination):
    folder_full_path = os.path.join(destination, folder)
    if os.path.isdir(folder_full_path):
        print(f"\n{folder} folder content:")
        for f in os.listdir(folder_full_path):
            print(f"  - {f}")

with open(os.path.join(path, "Organized files report.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sl No", "File Name", "Category", "Full Destination Path"])
    for i, (fname, dest_cat, full_dest) in enumerate(report_data, 1):
        writer.writerow([i, fname, dest_cat, full_dest])
