from .file import File

class Addenda(File):
    def __init__(self):
        super().__init__()

    def replace_values(self, content, options=None):
        if not options:
            return content

        for key, value in options.items():
            content = content.replace(key, value)

        return content

    def get_file_content(self, replace_values):
        file = self.get_file()
        file_content = file['content']
        
        return self.replace_values(file_content, replace_values)