import json

import pytest


def pytest_collect_file(parent, path):
    if path.ext == ".json" and path.basename.startswith("test"):
        return JsonFile(path, parent)


class JsonFile(pytest.File):
    def collect(self):
        with self.fspath.open() as jsonf:
            for word in json.load(jsonf):
                yield JsonItem(self, word)


class JsonItem(pytest.Item):
    def __init__(self, parent, word):
        super().__init__(word, parent)
        self.word = word

    def runtest(self):
        assert self.word != ""
