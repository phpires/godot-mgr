import json
import requests

from classes.godot_remote_tags import GodotRemoteTags
from functions.tags import tag_exists

def fetch_download_url(tag_name):
    
    if not tag_exists(tag_name):
        raise Exception("godot version does not exists.")
    api_url = f"https://api.github.com/repos/godotengine/godot/releases/tags/{tag_name}"
    
    headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "godot-downloader"
    }

    print(f"Fetching metadata from {api_url}")
    response = requests.get(url=api_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed while fetching godot v{tag_name} metadata")
    
    release = response.json()
    asset = None
    print(f"Getting windows asset")
    for a in release['assets']:
        if "win64.exe.zip" in a['name']:
            asset = a
            break

    if not asset:
        raise Exception("Could not find desired asset in release.")
    
    print(f"asset found.")

    download_url = asset['browser_download_url']
    print(f"download_url: {download_url}")

    file_name = asset['name']
    print(f"file_name: {file_name}")

    return download_url, file_name

def download_tags(tag_url):
    print(f"Downloading tags from url: {tag_url}")
    response = requests.get(url=tag_url)

    if not response.status_code == 200:
        raise Exception("Failed when downloading tags")
    
    parsed_result = json.loads(response.content)
    godot_remote_tags = []
    for r in parsed_result:
        godot_remote_tags.append(GodotRemoteTags(r["name"], r["zipball_url"], r["tarball_url"], r["commit"], r["node_id"]))
    return godot_remote_tags

def download_godot_version(tag_name):
    download_url, file_name = fetch_download_url(tag_name)
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("Download finished")
            