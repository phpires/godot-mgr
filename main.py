from functions.tags import download_tags, list_tags_names, load_tags, save_tags

def main():
    godot_remote_tags = load_tags()
    if not load_tags():
        godot_remote_tags = download_tags()
        save_tags(godot_remote_tags)
    #print(f"main>> godot_remote_tags:{godot_remote_tags}")
    print(list_tags_names(godot_remote_tags))
    
if __name__ == "__main__":
    main()