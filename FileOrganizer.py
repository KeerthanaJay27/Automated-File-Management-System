import os
import shutil
import csv

source = "D:\Automated File Management System"            
destination = "D:\Automated File Management System\\Sorted_Files" 

if not os.path.exists(destination):
    os.mkdir(destination)

log_file = os.path.join(destination, "Organized_Files_Report.csv")
if not os.path.exists(log_file):
    with open(log_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file_name", "status"])

file_types = {
    "Word Documents": [".doc", ".docx"],
    "Excel Files": [".xls", ".xlsx", ".csv"],
    "PowerPoint Files": [".ppt", ".pptx"],
    "PDFs": [".pdf"],
    "Text Files": [".txt", ".md"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".psd", ".ai", ".eps"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac", ".wmv"],
    "Video Files": [".mp4", ".mov", ".avi", ".mkv"],
    "Python Files": [".py"],
    "HTML / Web Files": [".html", ".htm", ".css", ".js", ".json", ".xml"],
    "Java Files": [".java"],
    "C / C++ Files": [".c", ".cpp", ".h"],
    "SQL Files": [".sql", ".mdb", ".accdb", ".parquet", ".avro"],
    "Compressed Files": [".zip", ".rar", ".tar", ".tar.gz"],
    "Config / Log Files": [".cfg", ".ini", ".conf", ".env", ".log", ".yaml", ".yml"],
    "CAD / Design Files": [".dwg", ".dxf", ".fig", ".sketch", ".stl", ".obj"]
}

for file_name in os.listdir(source):
    file_path = os.path.join(source, file_name)

    if os.path.isdir(file_path):
        continue

    ext = os.path.splitext(file_name)[1].lower()

    folder_name = "Others"
    for category, extensions in file_types.items():
        if ext in extensions:
            folder_name = category
            break

    organized_folder = os.path.join(destination, folder_name)
    if not os.path.exists(organized_folder):
        os.mkdir(organized_folder)

    shutil.copy2(file_path, os.path.join(organized_folder, file_name))

    print(f"Copied {file_name} → {folder_name} (Organized)")

    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([file_name, "Moved"])

print("All files are moved to respective folders. Please check.\nThankYou!!")