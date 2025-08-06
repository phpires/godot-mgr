#import sys
import typer
from typing_extensions import Annotated
#from functions.tags import load_tags, save_tags
#from functions.downloads import download_tags, download_godot_version

app = typer.Typer()
tag_url = "https://api.github.com/repos/godotengine/godot/tags"
tag_for_download = "4.4.1-stable"

@app.command()
def list():
    print("List remote tags!")
    pass

@app.command("download")
def download():
    print("Downloading tags!")
    pass

    
if __name__ == "__main__":
    app()