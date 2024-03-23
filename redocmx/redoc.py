from .service import Service
from .cfdi import Cfdi

class RedocmxClient:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.service = Service(self.api_key)

    @property
    def cfdi(self):
        return Cfdi()
