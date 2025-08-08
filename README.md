# Godot Manager CLI Tool
A simple CLI tool to manage godot versions on your local machine.

## Functionality overview
1. List downloaded tags
2. Download available tags
3. Download specific godot version using tag

## Basic Usage
1. List downloaded tags
On engine folder execute the command:
``uv run main.py tags``
This will list all of the available tags.

2. Download specific tag
On engine folder execute the command:
``uv run main.py download``
This will download the default version of Godot. Currently is setted to "4.4.1-stable"
If it is desired to download a specific tag use the command:
``uv run main.py download --tag <tag-version>``
Example:
``uv run main.py download --tag 4.4.1-stable`` will download "4.4.1-stable" version of godot
Download will be saved on the code folder.
If an unavailable tag is passed, the program will throw error code 1.