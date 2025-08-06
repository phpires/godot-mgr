class CliInput:
    def __init__(self, list_remote_tags: bool, tag_version: str, download_folder: str, list_downloaded: bool):
        self.list_remote_tags = list_remote_tags
        self.tag_version = tag_version
        self.download_folder = download_folder
        self.list_downloaded = list_downloaded
        pass