from classes.godot_remote_tags import from_repr
import os

DATA_DIR = "data"

GODOT_REMOTE_TAGS_NAME = "godot_remote_tags.txt"
GODOT_REMOTE_TAG_TXT_FILEPATH = os.path.abspath(os.path.join(DATA_DIR, GODOT_REMOTE_TAGS_NAME))

GODOT_DOWNLOADED_VERSIONS = "godot_downloaded_versions.txt"
GODOT_DOWNLOADED_VERSIONS_FILEPATH = os.path.abspath(os.path.join(DATA_DIR, GODOT_DOWNLOADED_VERSIONS))

def load_tags():
    return read_from_txt_file_into_list(GODOT_REMOTE_TAG_TXT_FILEPATH)

def load_downloaded_tags():
    return read_from_txt_file_into_list(GODOT_DOWNLOADED_VERSIONS_FILEPATH)

def save_remote_tags_available(godot_remote_tags):
    print(f"Saving remote tags available")
    create_dir(os.path.abspath(DATA_DIR))
    data = []
    for d in godot_remote_tags:
        data.append(str(d))
    write_on_txt_file(GODOT_REMOTE_TAG_TXT_FILEPATH, data)
    print(f"Remote available tags saved on filepath: {GODOT_REMOTE_TAG_TXT_FILEPATH}")

def list_remote_tags_downloaded(godot_remote_tags):
    tags_names = []
    for tag in godot_remote_tags:
        tags_names.append(tag.name)
    return tags_names

def print_to_user(godot_remote_tags):
    tag_list_by_name = ""
    for tag in godot_remote_tags:
        tag_list_by_name += tag.name + "\n"
    print(tag_list_by_name)

def tag_exists_on_remote(tag_name):
    existing_tags = list_remote_tags_downloaded(load_tags())
    if not (tag_name in existing_tags):
        return False
    return True

def save_downloaded_tag_version(tag_name):
    print(f"Saving downloaded tag.")
    create_dir(os.path.abspath(DATA_DIR))
    append_on_txt_file(GODOT_DOWNLOADED_VERSIONS_FILEPATH, [tag_name])
    print(f"Downloaded tag saved on filepath: {GODOT_DOWNLOADED_VERSIONS_FILEPATH}")

def create_dir(dir_path):
    print(f'Creating dir on {dir_path}')
    dir = os.path.abspath(dir_path)
    if not os.path.isdir(dir):
        print(f"Dir {dir} not found. Creating...")
        os.mkdir(dir)
        print(f"{dir} created.")
    else:
        print(f"Dir {dir} already exists. Nothing was done.")

def write_on_txt_file(filepath, data):
    print(f"Writing data to a txt file on filepath: {filepath}")
    with open(filepath, "w+") as f:
        f.write("\n".join(data))

def append_on_txt_file(filepath, data):
    print(f"Appending data on txt file on filepath: {filepath}")
    with open(filepath, "a") as f:
        for d in data:
            f.write("%s"%d)

def read_from_txt_file_into_list(filepath):
    try:
        data = []
        print(f"Opening file on {filepath}")
        with open(filepath, "r") as file:
            for line in file.readlines():
                print(f"line: {line}")
                data.append(from_repr(line))
                print(f"data: {data}")
        return data
    except FileNotFoundError:
        print(f"File not found on {filepath}")
        return None