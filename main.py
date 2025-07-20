import subprocess
def main():
    result = subprocess.run(["curl", "https://api.github.com/repos/godotengine/godot/tags"], capture_output=True, text=True)
    print(result.stdout)
    
if __name__ == "__main__":
    main()