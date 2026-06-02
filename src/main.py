import sys
import typer
from typing_extensions import Annotated
from functions.tags import load_tags, save_remote_tags_available, tag_exists_on_remote, print_to_user, save_downloaded_tag_version, load_downloaded_tags
from functions.downloads import download_tags_from_remote, download_godot_version
from classes.godot_remote_tags import GodotRemoteTags

app = typer.Typer()
tag_url = "https://api.github.com/repos/godotengine/godot/tags"

@app.command("versions")
def list():
    tags: GodotRemoteTags = update_local_tags()
    print("Available versions to download are: ")
    print_to_user(tags)

@app.command("download")
def download(tag: Annotated[str, typer.Option(help="Godot version to download.")] = None):
    tags: GodotRemoteTags = update_local_tags()
    downloaded_tags: GodotRemoteTags = load_downloaded_tags()

    if not tag:
        print(f"No godot version were given for donwload. Using the latest version: {tags[0].name}")
        tag = tags[0].name
    elif not tag_exists_on_remote(tag):
        print("Tag does not exists.")
        sys.exit(1)
        
    if not downloaded_tags or not (tag in downloaded_tags):
        download_godot_version(tag)
        save_downloaded_tag_version(tag)
        return
    print(f"Godot version already downloaded.")
    
def update_local_tags():
    tags = download_tags_from_remote(tag_url)
    save_remote_tags_available(tags)
    return tags
    
if __name__ == "__main__":
    app()