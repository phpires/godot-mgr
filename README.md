# Godot Manager CLI Tool
A simple CLI tool to manage godot versions on your local machine.

## Functionality overview
1. List versions
2. Download
3. Delete
4. Help

## Basic Usage
**1. List versions**

On engine folder execute the command:

``uv run main.py versions``

This will list all of the available tags.

If you want to check if there are any local versions downloaded, run the command:

``uv run main.py versions --local`` or ``uv run main.py versions -l``

**2. Download**

On engine folder execute the command:

``uv run main.py download``

This will download the last released version of Godot.

For a specific version use the command:

``uv run main.py download --tag <tag-version>`` or ``uv run main.py download -t <tag-version>``

Example:

``uv run main.py download --tag 4.4.1-stable`` will download "4.4.1-stable" version of godot

Download will be saved on 'godot' folder located inside project.

If an unavailable tag is passed, the program will throw error code and no download will be made.

**3. Delete**

Delete a downloaded Godot version with the command:

``uv run main.py delete --tag <tag-version>`` or
``uv run main.py delete -t <tag-version>`` 

A tag must be passed, otherwise a error will occur.

For clearing all downloaded godots execute:

``uv run main.py delete --clear`` or ``uv run main.py delete -c``

**4. Help**

To check available commands use the help command:

``uv run main.py --help``

## Future Implementations

Working on a execute command to run godot on CLI.