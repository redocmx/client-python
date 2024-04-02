from .pdf import Pdf
from .service import Service
from .file import File
from .addenda import Addenda

class Cfdi(File):
    def __init__(self):
        super().__init__()
        self.pdf = None
        self.addenda = None
        self.addenda_replace_values = None
        self.service = Service.get_instance()

    def set_addenda(self, addenda, replace_values=None):
        if addenda and not isinstance(addenda, Addenda):
            raise TypeError('addenda must be an instance of Addenda.')
        if replace_values and not isinstance(replace_values, dict):
            raise TypeError('Addenda replace values must be a valid key-value object.')

        self.addenda = addenda
        self.addenda_replace_values = replace_values

    def to_pdf(self, payload={}):
        if self.pdf:
            return self.pdf
        
        if not isinstance(payload, dict):
            raise TypeError('toPdf function only accepts an object as a parameter.')

        file = self.get_file()

        if self.addenda:
            addenda_content = self.addenda.get_file_content(self.addenda_replace_values)
            payload['addenda'] = addenda_content

        payload['format'] = 'pdf'

        result = self.service.cfdis_convert(file['content'], payload)
        self.pdf = Pdf(result)

        return self.pdf

