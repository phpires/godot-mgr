from classes.godot_remote_tags import from_repr
import os

def load_tags():
    godot_remote_tags = []
    engine_data_dir = os.path.abspath("engine/data")
    if not os.path.isdir(engine_data_dir):
        print(f"Dir for saving tags not found. Creating...")
        os.mkdir(engine_data_dir)
        print("Engine data dir created.")
    try:
        with open("engine/data/godot_remote_tags.txt", "r") as file:
            for line in file.readlines():
                godot_remote_tags.append(from_repr(line))
        return godot_remote_tags
    except FileNotFoundError:
        print("No tags were found.")
        return None

def save_tags(godot_remote_tags):
    print(f"Saving tags")
    filepath = "engine/data/godot_remote_tags.txt"
    with open(filepath, "w") as file:
        lines = []
        for remote_tag in godot_remote_tags:
            lines.append(str(remote_tag))
        file.writelines(lines)
    print(f"Tags saved on filepath: {filepath}")

def list_tags_names(godot_remote_tags):
    tags_names = []
    for tag in godot_remote_tags:
        tags_names.append(tag.name)
    return tags_names

def print_to_user(godot_remote_tags):
    tag_list_by_name = ""
    for tag in godot_remote_tags:
        tag_list_by_name += tag.name + "\n"
    
    print(tag_list_by_name)

def tag_exists(tag_name):
    existing_tags = list_tags_names(load_tags())
    if not (tag_name in existing_tags):
        return False
    return True