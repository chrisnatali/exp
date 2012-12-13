import os
import fnmatch

def folder_file_iter(root, file_match):
    folders = os.walk(root).next()[1]
    for folder in folders:
        full_folder = os.path.join(root, folder)
        for filename in fnmatch.filter(os.listdir(full_folder), file_match):
            full_file = os.path.join(full_folder, filename)
            yield full_folder, full_file

