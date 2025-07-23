import re

class GodotRemoteTags:

    def __init__(self, name, zipball_url, tarball_url, commit, node_id):
        self.name = name
        self.zipball_url = zipball_url
        self.tarball_url = tarball_url
        self.commit_sha, self.commit_url = commit["sha"], commit["url"]
        self.node_id = node_id
    
    def __repr__(self):
        return f"GodotRemoteTags(name={self.name}, zipball_url={self.zipball_url}, tarball_url={self.tarball_url}, commit_sha={self.commit_sha}, node_id={self.node_id})\n"
    
def from_repr(list_of_repr_remote_tags):
    
    pattern = re.compile(r'''
        GodotRemoteTags\(
        \s*name=(?P<name>[^,]+),
        \s*zipball_url=(?P<zip>[^,]+),
        \s*tarball_url=(?P<tar>[^,]+),
        \s*commit_sha=(?P<sha>[0-9a-f]+),
        \s*node_id=(?P<node>[^)]+)
        \)
    ''', re.VERBOSE)

    tags = []
    for m in pattern.finditer(list_of_repr_remote_tags):
        name = m.group('name')
        zip_url = m.group('zip')
        tar_url = m.group('tar')
        sha = m.group('sha')
        node_id = m.group('node')
        commit = {"sha": sha, "url": f"https://api.github.com/git/commits/{sha}"}
        tags.append(GodotRemoteTags(name, zip_url, tar_url, commit, node_id))
    return tags