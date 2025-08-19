import json

class BaseFileSystem:
    def __init__(self, data, dir = None):
        self.dir = dir
        self.data = data
        pass
    
    def to_json(self):
        return json.dumps(self.data)
    
    def save(self):
        # 1 - transform to json
        if (self.data is None):
            raise ValueError("data is empty.")
        print(json.dumps(self.data))
        # 2 - save as binary
        # 2.1 - create new if none
        # 2.2 - append if there are already
        pass

