import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist!")
        return
    
    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Move files to corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    print(f"Moved: {filename} -> {category}/")
                    break
    
    print("File organization complete!")

if __name__ == "__main__":
    folder_path = input("Enter the directory path to organize: ")
    organize_files(folder_path)

# README.md
README_CONTENT = """
# File Organizer

A Python script to organize files into categorized folders based on their extensions.

## Features
- Automatically moves files into categories (Images, Documents, Videos, etc.).
- Supports multiple file formats.
- Easy to use: Just provide the directory path.

## Usage
```bash
python organizer.py
```
Then enter the directory path you want to organize.

## Requirements
- Python 3.x

## License
MIT License
"""

with open("README.md", "w") as readme_file:
    readme_file.write(README_CONTENT)

print("README.md file created!")
