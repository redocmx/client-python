from .pdf import Pdf
from .service import Service
from pathlib import Path

class Cfdi:
    def __init__(self):
        self.pdf = None
        self.addenda = None
        self.file_path = None
        self.file_content = None
        self.service = Service.get_instance()

    def from_file(self, file_path):
        self.file_path = file_path
        return self

    def from_string(self, file_content):
        self.file_content = file_content
        return self

    def to_pdf(self, payload={}):
        if self.pdf:
            return self.pdf

        file_content = self._get_xml_content()
        payload['format'] = 'pdf'

        if self.addenda:
            payload['addenda'] = self.addenda

        result = self.service.cfdis_convert(file_content, payload)
        self.pdf = Pdf(result)

        return self.pdf

    def _get_xml_content(self):
        if self.file_content:
            return self.file_content
        elif self.file_path:
            path = Path(self.file_path)
            if not path.exists() or not path.is_file():
                raise FileNotFoundError(f"Failed to read XML content from file: {self.file_path}. The file does not exist.")
            return path.read_text()
        else:
            raise ValueError("XML content for the CFDI must be provided.")

    def set_addenda(self, addenda):
        if not isinstance(addenda, str):
            raise TypeError("setAddenda function only accepts a string parameter.")
        self.addenda = addenda
