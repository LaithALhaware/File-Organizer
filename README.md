# File Organizer

A simple Python script to automatically organize files into categorized folders based on their extensions.

## Features
- Moves files into categories (Images, Documents, Videos, etc.).
- Supports multiple file formats.
- Easy to use: Just provide the directory path.

## Installation
No external dependencies are required. This script runs with standard Python libraries.

## Usage
1. Run the script:
   ```bash
   python organizer.py
   ```
2. Enter the directory path you want to organize.
3. The script will sort the files into appropriate folders.

## Example
Before:
```
Downloads/
├── photo.jpg
├── document.pdf
├── song.mp3
```
After running the script:
```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── document.pdf
├── Music/
│   └── song.mp3
```

## Requirements
- Python 3.x
