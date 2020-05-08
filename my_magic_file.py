import os.path
import tempfile

class File():
    def __init__(self, path):
        self._path = path
        self._iter = None
        if not os.path.exists(self._path):
            f = open(self._path, 'x')
            f.close()

    def __str__(self):
        return self._path

    def __add__(self, obj):
        path = os.path.join(tempfile.gettempdir(), \
                            self._path)
        _file_obj = File(path)
        _file_obj.write(self.read() + obj.read())
        return _file_obj

    def __iter__(self):
        self._iter = open(self._path, 'r')
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration

        result = self._iter.readline()
        if not result:
            self._iter.close()
            raise StopIteration

        return result

    def read(self):
        with open(self._path, 'r') as f:
            return f.readline()

    def write(self, text):
        with open(self._path, 'w') as f:
            return f.write(text)
