 # Automated File Organizer - CODTECH Task 1

This Python project automatically organizes files in Downloads folder based on file type.

## Features
- Organizes Images, Documents, Videos, Music, Programs, Archives
- Creates folders automatically if not exist
- Moves unknown files to 'Others' folder
- Shows total count of files organized

## Technologies Used
- **Python** - Programming language
- **os module** - For folder operations like makedirs, listdir, path
- **shutil module** - For moving files using shutil.move

## How to Run
1. Change "source_folder"path in main.py to your folder path
2. Run: `python main.py`

## Output Example
Organizing folder: C:/Users/satya/Downloads
Total files found: 8
Moved: desktop.ini → Others
Moved: python-manager-26.2.msix → Programs

## Project Flow
Files → Python Script → Detect File Type → Move to Respective Folder

## Author
Satya - CODTECH Internship Task 1