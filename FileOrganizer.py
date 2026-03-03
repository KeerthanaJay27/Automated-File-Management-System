import os
import shutil
import csv

source = r"D:\Automated File Management System Project"            
destination = r"D:\Automated File Management System Project\Sorted_Files" 

os.makedirs(destination, exist_ok=True)

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

count = 0 

with open(log_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for file_name in os.listdir(source):
        file_path = os.path.join(source, file_name)

        if os.path.isdir(file_path) or file_name == "Sorted_Files" or file_name == "Organized_Files_Report.csv":
            continue

        ext = os.path.splitext(file_name)[1].lower()

        folder_name = "Others"
        for category, extensions in file_types.items():
            if ext in extensions:
                folder_name = category
                break

        organized_folder = os.path.join(destination, folder_name)
        
        os.makedirs(organized_folder, exist_ok=True)

        shutil.copy2(file_path, os.path.join(organized_folder, file_name))
        
        count += 1
        print(f"[{count}] Copied {file_name} → {folder_name}")

        writer.writerow([file_name, "Copied"])

print(f"\nTask Complete: {count} files backed up and organized.\nThank You!!")
