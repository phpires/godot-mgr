import sys
import typer
import platform

from typing_extensions import Annotated

from functions.tags import print_downloaded_godot_versions, tag_exists_on_local, save_remote_tags_available, tag_exists_on_remote, print_available_versions_to_download, save_downloaded_tag_version, load_downloaded_tags
from functions.downloads import download_tags_from_remote, download_godot_version
from functions.delete import delete_godot, clear_download_folder

from classes.godot_remote_tags import GodotRemoteTags

app = typer.Typer()
tag_url = "https://api.github.com/repos/godotengine/godot/tags"

@app.command("versions")
def list(local: Annotated[bool, typer.Option("-l", "--local", help="List downloaded Godot versions")] = False):
    if local:
        print_downloaded_godot_versions()
        sys.exit(0)
    tags: GodotRemoteTags = update_local_tags()
    print_available_versions_to_download(tags)

@app.command("download")
def download(tag: Annotated[str, typer.Option("-t", "--tag", help="Godot version to download.")] = None):
    tags: GodotRemoteTags = update_local_tags()
    
    if not tag:
        print(f"No godot version were given for donwload. Using the latest version: {tags[0].name}")
        tag = tags[0].name
    elif not tag_exists_on_remote(tag):
        print("Tag does not exists.")
        sys.exit(1)
    
    if not tag_exists_on_local(tag):
        download_godot_version(tag)
        save_downloaded_tag_version(tag)
        return
    
    print(f"Godot version {tag} already downloaded.")

@app.command("delete")
def delete(tag: Annotated[str, typer.Option("-t", "--tag", help="Godot version to delete.")] = None,
           clear: Annotated[bool, typer.Option("-c", "--clear", help="Delete all godot versions downloaded.")] = False):
    if not tag and not clear:
        print("Must give a godot version to delete")
        sys.exit(1)
    if not tag_exists_on_local(tag) and not clear:
        print(f'Godot not found for version: {tag}')
        sys.exit(1)
    if clear:
        proceed = typer.confirm("Clear will remove ALL versions of Godot. Do you want to proceed?")
        if not proceed:
            sys.exit(1)
        clear_download_folder()
        sys.exit(0)
    delete_godot(tag)

#@app.command("execute")
def execute():
    print(platform.system())
    pass

def update_local_tags():
    tags = download_tags_from_remote(tag_url)
    save_remote_tags_available(tags)
    return tags
    
if __name__ == "__main__":
    app()