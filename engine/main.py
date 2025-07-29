from functions.tags import list_tags_names, load_tags, save_tags
from functions.downloads import download_tags, download_godot_version

def main():
    #tag_url = os.environ.get("GITHUB_GODOT_TAGS_URL")
    tag_url = "https://api.github.com/repos/godotengine/godot/tags"
    if not load_tags():
        print(f"Tags not found on system. Fetching available tags from remote.")
        save_tags(download_tags(tag_url))
    tag_for_download = "4.4.1-stable"
    print(f"Downloading Godot version {tag_for_download}")
    download_godot_version(tag_for_download)
    
if __name__ == "__main__":
    main()