from .service import Service
from .cfdi import Cfdi
from .addenda import Addenda

class RedocmxClient:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.service = Service(self.api_key)

    @property
    def cfdi(self):
        return Cfdi()
    
    @property
    def addenda(self):
        return Addenda()
