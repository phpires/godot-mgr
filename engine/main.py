import sys
import typer
from typing_extensions import Annotated
from functions.tags import load_tags, save_tags, tag_exists, print_to_user
from functions.downloads import download_tags, download_godot_version
from classes.godot_remote_tags import GodotRemoteTags

app = typer.Typer()
tag_url = "https://api.github.com/repos/godotengine/godot/tags"
DEFAULT_VERSION = "4.4.1-stable"

@app.command("tags")
def list():
    print("Listing available tags...")
    tags: GodotRemoteTags = load_tags()
    if not tags:
       print("No tags on filesystem. Downloading from remote.")
       tags = download_tags(tag_url)
       save_tags(tags)
    print("Available tags to download are: ")
    print_to_user(tags)

@app.command("download")
def download(tag: Annotated[str, typer.Option(help="Godot version to download.")] = None):
    if not tag_exists(tag):
        print("Tag does not exists.")
        sys.exit(1)
    if tag:
        download_godot_version(tag)
    else:
        #TODO: Load a default version if not defined
        download_godot_version(DEFAULT_VERSION)
    #TODO: save downloaded tags and the folder of destination. Database?
    

    
if __name__ == "__main__":
    app()