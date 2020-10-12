import os
from pathlib import Path
import shutil

DIRECTORIES_MAP = {
    "/Documents/$Downloaded Docs": [".docx", ".doc", ".odt", ".rtf", ".xls", ".xlsx", ".ppt", "pptx", ".txt", ".pdf"],
    "/Documents/$Downloaded Archives": [".iso", ".tar", ".gz", ".7z", ".rar", ".zip"],
    "/Documents/$Downloaded Folders": ["dir"],
    "/Documents/$Downloaded Other": ["other"],
    "/Pictures/$Downloaded": [".jpeg", ".jpg", ".gif", ".bmp", ".png"],
    "/Music/$Downloaded": [".mp3", ".wav"],
    "/Videos/$Downloaded": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".mpg", ".mpeg"],
}

HOME_PATH = str(Path.home())

DOWNLOADS_PATH = HOME_PATH + '/Downloads'

FILE_FORMATS = {file_format: HOME_PATH + directory
                for directory, file_formats in DIRECTORIES_MAP.items()
                for file_format in file_formats}


def autorganize_stuff():
    # remove empty folders
    for dir in os.scandir(DOWNLOADS_PATH):
        try:
            os.rmdir(dir)
        except:
            pass

    for entry in os.scandir(DOWNLOADS_PATH):
        file_path = Path(entry)
        file_name = os.path.basename(file_path)
        if entry.is_dir():
            file_format = 'dir'
        else:
            file_format = file_path.suffix.lower()
            if file_format not in FILE_FORMATS:
                file_format = 'other'
        move_to_assigned_folder(file_format, file_path, file_name)


def move_to_assigned_folder(file_format, file_path, file_name):
    directory_path = Path(FILE_FORMATS[file_format])
    directory_path.mkdir(exist_ok=True)
    shutil.move(file_path, str(directory_path) + '/' + file_name)


if __name__ == "__main__":
    autorganize_stuff()
