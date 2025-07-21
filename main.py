import subprocess
import json
from classes.godot_remote_tags import GodotRemoteTags

def main():
    result = subprocess.run(["curl", "https://api.github.com/repos/godotengine/godot/tags"], capture_output=True, text=True)
    parsed_result = json.loads(result.stdout)
    godot_remote_tags = []
    for r in parsed_result:
        godot_remote_tags.append(GodotRemoteTags(r["name"]))
    
if __name__ == "__main__":
    main()