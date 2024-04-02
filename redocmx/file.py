from pathlib import Path

class File:
    def __init__(self):
        self.file_path = None
        self.file_content = None

    def from_file(self, file_path):
        self.file_path = file_path
        return self

    def from_string(self, file_content):
        self.file_content = file_content
        return self

    def get_file(self):
        if self.file_content:
            return { 'content': self.file_content }

        elif self.file_path:
            path = Path(self.file_path)
            if not path.exists() or not path.is_file():
                raise FileNotFoundError(f"Failed to read XML content from file: {self.file_path}. The file does not exist.")
            
            self.file_content = path.read_text()
            return { 'content': self.file_content }
        else:
          raise ValueError(f"Failed to load file {self.__class__.__name__}, you must use from_file or from_string.")

