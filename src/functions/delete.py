from re import escape, search
from os import listdir, remove
from os.path import isfile, abspath, join

GODOT_FOLDER_PATH = abspath("godot")
def delete_godot(tag):
    all_godots = list_files_from_folder(GODOT_FOLDER_PATH)
    escaped_tags = escape(tag)
    pattern  = rf"Godot_v{escaped_tags}.*$"
    deleted = delete_from_list_by_pattern(pattern, all_godots)
    if deleted:
        print(f"Deleted: {deleted}")
        clear_from_godot_downloaded_list(tag)
    else:
        print(f"No Godot installation found for tag: {tag}")
        return

def list_files_from_folder(folder_path):
    files = []
    for f in listdir(folder_path):
        if isfile(join(folder_path, f)):
            files.append(f)
    return files

def delete_from_list_by_pattern(pattern, str_list):
    deleted = []
    for str in str_list:
        if search(pattern, str):
            remove(join(GODOT_FOLDER_PATH, str))
            deleted.append(str)
    return deleted


def clear_from_godot_downloaded_list(tag):
    filepath = "data/godot_downloaded_versions.txt"
    try:
        data = []
        print(f"Opening file on {filepath}")
        with open(filepath, "r+") as file:
            for line in file.readlines():
                stripped = line.strip()
                print(f"line: {stripped}")
                if tag == stripped:
                    continue
                data.append(stripped)
                print(f"data: {data}")
            file.seek(0)
            file.write("\n".join(data))
            file.truncate()
        return data
    except FileNotFoundError:
        print(f"File not found on {filepath}")
        return None  
    
    