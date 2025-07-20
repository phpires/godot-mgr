class GodotRemoteTags:

    def __init__(self, name, zipball_url, tarball_url, commit, node_id):
        self.name = name
        self.zipball_url = zipball_url
        self.tarball_url = tarball_url
        self.commit_sha, self.commit_url = commit["sha"], commit["url"]
        self.node_id = node_id
