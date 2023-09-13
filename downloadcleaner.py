"""
3rd complete rewrite. Now with pathlib and much simpler - 2023-09-12
Python 3.10
Goes through your files in Downloads folder and moves them into own subfolders
"""
from pathlib import Path
import collections

BASE_PATH = Path.home()
DOWNLOADS_PATH = BASE_PATH.joinpath("Downloads")

""" In below dict, keys are folders to be created and the associated list is file extensions to move."""
FILE_TYPES = {"Pictures": [".png", ".jpg", ".jpeg", ".JPG", ".webp", ".svg", ".dwg", ".PNG"],
              "Documents": [".pdf", ".docx", ".pptx", ".txt", ".xlsx", ".doc", ".xls"],
              "3D": [".stl", ".f3d", ".STEP", ".stp", ".3mf", ".blend", ".SAT"],
              "Archives": [".zip", ".dmg", ".pkg", ".rar", ".deb", ".gz"],
              "Music": [".wma", ".mp3"],
              "Movies": [".mov", ".mp4"],
              "Others": [".srt", ".curaprofile", ".html"],
              "DELETE ME": [".ics", ".torrent"]
              }


def list_files():
    files_mapping = collections.defaultdict(list)
    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file() and file.suffix != "":
            file_name, file_ext = file.name, file.suffix
            files_mapping[file_ext].append(file_name)
    return files_mapping


def move_files(list_of_files):
    for destination_folder, suffixes in FILE_TYPES.items():
        for suffix in suffixes:
            if suffix in list_of_files.keys():
                make_folder(destination_folder)
                for file in list_of_files[suffix]:
                    Path(DOWNLOADS_PATH / file).rename(DOWNLOADS_PATH / destination_folder / file)
                    print(f"\033[1mMoved\033[0m {file}\033[33m to \033[3m{destination_folder}\033[0m")
            else:
                pass


def make_folder(destination):
    if not Path.joinpath(DOWNLOADS_PATH, destination).is_dir():
        print(f"\n{destination} doesn't exist, let's make one!\n")
        Path.mkdir(DOWNLOADS_PATH / destination)
    else:
        print(f"\n\033[33m{destination} folder already in \033[0m{DOWNLOADS_PATH}\n")

def count_files(list_of_files):
    sorted_dict = dict(sorted(list_of_files.items(), key=lambda item: len(item[1]), reverse=True))
    print(f"Found {len(list_of_files.keys())} different file extensions\n")
    for suffix in sorted_dict:
        print(f"{len(list_of_files[suffix])}", end=" ")
        if len(list_of_files[suffix]) == 1:
            print(f"file", end=" ")
        else:
            print(f"files", end=" ")
        print(f"with {suffix} extension")



def main():
    print(f"""
    {BASE_PATH = }
    {DOWNLOADS_PATH = }
    """)

    listed_files = list_files()
    count_files(listed_files)
    move_files(listed_files)


if __name__ == "__main__":
    main()
