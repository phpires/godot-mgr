from classes.godot_remote_tags import from_repr
import os

DATA_DIR = "data"

GODOT_REMOTE_TAGS_NAME = "godot_remote_tags.txt"
GODOT_REMOTE_TAG_TXT_FILEPATH = os.path.abspath(os.path.join(DATA_DIR, GODOT_REMOTE_TAGS_NAME))

GODOT_DOWNLOADED_VERSIONS = "godot_downloaded_versions.txt"
GODOT_DOWNLOADED_VERSIONS_FILEPATH = os.path.abspath(os.path.join(DATA_DIR, GODOT_DOWNLOADED_VERSIONS))

def load_tags():
    godot_remote_tags = []
    try:
        with open(GODOT_REMOTE_TAG_TXT_FILEPATH, "r") as file:
            for line in file.readlines():
                godot_remote_tags.append(from_repr(line))
        return godot_remote_tags
    except FileNotFoundError:
        print("No tags were found.")
        return None

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
    print(f"Saving remote tags available")
    dir = os.path.abspath(dir_path)
    if not os.path.isdir(dir):
        print(f"Dir {dir} not found. Creating...")
        os.mkdir(dir)
        print(f"{dir} created.")
    else:
        print(f"Dir {dir} already exists. Nothing was done.")

def write_on_txt_file(filepath, data):
    print(f"filepath: {filepath}")
    with open(filepath, "w+") as f:
        f.write("\n".join(data))

def append_on_txt_file(filepath, data):
    with open(filepath, "a") as f:
        f.write("\n".join(data))