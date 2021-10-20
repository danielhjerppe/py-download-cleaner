import collections
import os
from pprint import pprint

"""Downloads folder cleaner
Made by Daniel Hjerppe daniel.hjerppe@gmail.com
Heavily influenced by Curious Coding: https://www.youtube.com/watch?v=5idxowRxWW0

Tested on MacOS Big Sur and Windows 10

Goes through your files in Downloads folder and moves them into own subfolders under Downloads
Moves folders to own sub-folder "Folders"

"""

# File categories. Feel free to add your own.
EXT_AUDIO = ["mp3", "wav", "aif", "aiff", "flac"]
EXT_VIDEO = ["mp4", "mov"]
EXT_IMGS = ["png", "PNG", "jpg", "JPG", "jpeg", "gif", "webp", "psd", "eps", "ai"]
EXT_DOCS = ["txt", "pdf", "PDF", "doc", "docx", "xls", "xlsx", "pptx", "rtf", "ppt", "epub"]
EXT_COMPR = ["zip", "rar", "bin"]
EXT_INSTL = ["dmg", "iso", "pkg", "app", "exe"]
EXT_OTHER = ["ics", "otf"]
EXT_DELETE = ["torrent"]

# Working paths. No need to change if folders in default locations
BASE_PATH = os.path.expanduser("~")  # Gets your user folder
DOWNLOADS_PATH = os.path.join(BASE_PATH, "Downloads")  # Name of your downloads folder
# Destination folders to create
DEST_DIRS = ["Music", "Movies", "Pictures", "Documents", "Installers", "Others", "Zip", "Folders", "WeTrnsfr"]

# Print statements for debugging
print("BASE_PATH is", BASE_PATH)
print("DOWNLOADS_PATH is", DOWNLOADS_PATH)

for d in DEST_DIRS:
    # print(d)  # Debugging Prints folders to move files to
    dir_path = os.path.join(DOWNLOADS_PATH, d)
    if not os.path.isdir(dir_path):  # If folders not found, make them
        os.mkdir(dir_path)

print("DEST_DIRS is", DEST_DIRS)

files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

# print("files_mapping =", files_mapping)
print("Found the following files:")
print("files_list =")
# print(*files_list, sep="\n")
pprint(files_list)


for file_name in files_list:
    if file_name[0] != ".":
        file_ext = file_name.split(".")[-1]
        files_mapping[file_ext].append(file_name)

# pprint(files_mapping)

for f_ext, f_list in files_mapping.items():
    # print(f_ext)
    # print(f_list)
    if f_ext in EXT_INSTL:
        for file in f_list:
            print("f_list is:", f_list)
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Installers", file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(DOWNLOADS_PATH, "Installers", file))
            print("Files moved:", file)

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Pictures", file))
            print(os.path.join(DOWNLOADS_PATH, file))
            print(os.path.join(DOWNLOADS_PATH, "Pictures", file))
            print("Files moved:", file)

    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Documents", file))
            print("Files moved:", file)

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Music", file))
            print("Files moved:", file)

    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Zip", file))
            print("Files moved:", file)

    elif f_ext in EXT_OTHER:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Others", file))
            print("Files moved:", file)

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(DOWNLOADS_PATH, "Movies", file))
            print("Files moved:", file)

    elif f_ext in EXT_DELETE:
        for file in f_list:
            # print(os.path.isfile(os.path.join(DOWNLOADS_PATH, file)))
            if os.path.isfile(os.path.join(DOWNLOADS_PATH, file)):
                os.remove(os.path.join(DOWNLOADS_PATH, file))
            else:
                print("Error deleting file %s" % file)

"""Move lonely folders into subfolder Folders"""

for d in files_list:  # Move loose folders into own folder
    if "wetransfer" in d:
        print("WeTransfer! %s" % d)
        print("Moving WeTransfer folders to somewhere else...")
        if os.path.isdir(os.path.join(DOWNLOADS_PATH, d)):
            os.rename(os.path.join(DOWNLOADS_PATH, d), os.path.join(DOWNLOADS_PATH, "WeTrnsfr", d))
        else:
            print("No wetransfer folders found")

    elif d not in DEST_DIRS:
        # print("Kansiotesti true %s" % d)
        kansiopolku = os.path.join(DOWNLOADS_PATH, d)
        # print("IS DIR:", os.path.isdir(kansiopolku))
        if os.path.isdir(os.path.join(DOWNLOADS_PATH, d)):
            print("Moving folder %s to Folders" % d)
            os.rename(os.path.join(DOWNLOADS_PATH, d), os.path.join(DOWNLOADS_PATH, "Folders", d))
        else:
            print("%s is not an orphan folder" % d)
    else:
        if os.path.isdir(os.path.join(DOWNLOADS_PATH, d)):
            print("No home was found for folder %s" % d)
        elif os.path.isfile(os.path.join(DOWNLOADS_PATH, d)):
            print("No home was found for file %s" % d)
        else:
            pass
