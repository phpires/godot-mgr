import subprocess
import json
import os
from classes.godot_remote_tags import GodotRemoteTags, from_repr

def load_tags():
    godot_remote_tags = []
    with open("data/godot_remote_tags.txt", "r") as file:
        godot_remote_tags = from_repr(file.readlines())
    return godot_remote_tags
    

def save_tags(godot_remote_tags):
    print(f"Saving tags: {godot_remote_tags}")
    with open("data/godot_remote_tags.txt", "w") as file:
        lines = []
        for remote_tag in godot_remote_tags:
            lines.append(str(remote_tag))
        file.writelines(lines)

def download_tags():
    result = subprocess.run(["curl", os.environ.get("GITHUB_GODOT_TAGS")], capture_output=True, text=True)
    parsed_result = json.loads(result.stdout)
    godot_remote_tags = []
    for r in parsed_result:
        godot_remote_tags.append(GodotRemoteTags(r["name"], r["zipball_url"], r["tarball_url"], r["commit"], r["node_id"]))
    return godot_remote_tags

def list_tags_names(godot_remote_tags):
    tags_names = []
    for tag in godot_remote_tags:
        tags_names.append(tag.name)
    return tags_names