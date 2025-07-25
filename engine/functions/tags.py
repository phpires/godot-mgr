from classes.godot_remote_tags import from_repr

def load_tags():
    godot_remote_tags = []
    with open("engine/data/godot_remote_tags.txt", "r") as file:
        for line in file.readlines():
            godot_remote_tags.append(from_repr(line))
    return godot_remote_tags

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

def tag_exists(tag_name):
    existing_tags = list_tags_names(load_tags())
    if not (tag_name in existing_tags):
        return False
    return True