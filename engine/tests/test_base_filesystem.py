import sys
import os
# add project root to module search path so `engine` package is importable
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not os.path.isdir(os.path.join(_root, 'engine')):
    # handle case tests live under engine/tests
    _root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, _root)
import unittest
from engine.filesystem.base_filesystem import BaseFileSystem

class TestBaseFileSystem(unittest.TestCase):
    def testToJson(self):
        x = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        base_file_system = BaseFileSystem(x)
        as_json = base_file_system.to_json()
        print(as_json)
        
if __name__ == '__main__':
    unittest.main()