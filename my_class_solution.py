class FileReader:

    def __init__(self, path):
        try:
            with open(path, 'r') as file:
                self.data = file.read()
        except FileNotFoundError:
            self.data = ''

    def read(self):
        return self.data
