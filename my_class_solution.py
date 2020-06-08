class FileReader:

    def __init__(self, path):
        try:
            with open(path, 'r') as file:
                self.data = file.read()
        except FileNotFoundError:
            self.data = ''

    def read(self):
        return self.data

##class FileReader:
##    """Класс FileReader помогает читать из файла"""
##
##    def __init__(self, file_path):
##        self.file_path = file_path
##
##    def read(self):
##        try:
##            with open(self.file_path) as f:
##                return f.read()
##        except IOError:
##            return ""
