import requests
import base64
import json
import os

class Service:
    instance = None

    def __init__(self, api_key=None):
        if Service.instance is not None:
            raise Exception("You cannot create more than one instance!")
        self.api_key = api_key or os.getenv('REDOC_API_KEY')
        self.api_url = os.getenv('REDOC_API_URL', 'https://api.redoc.mx/cfdis/convert')
        Service.instance = self

    @classmethod
    def get_instance(cls, api_key=None):
        if cls.instance is None:
            cls.instance = Service(api_key)
        return cls.instance

    def cfdis_convert(self, file_content, payload):
        headers = {
            'Accept': 'application/pdf',
            'X-Redoc-Api-Key': self.api_key,
        }

        files = {
            'xml': ('document.xml', file_content, 'text/xml')
        }

        if 'style_pdf' in payload:
            files['style_pdf'] = (None, payload['style_pdf'])
        if 'addenda' in payload:
            files['addenda'] = (None, payload['addenda'])

        response = requests.post(self.api_url, files=files, headers=headers)

        if response.status_code != 200:
            raise Exception(f"HTTP error! status: {response.status_code}")

        buffer = response.content
        transaction_id = response.headers.get('x-redoc-transaction-id')
        totalPages = response.headers.get('x-redoc-pdf-total-pages')
        totalTime = response.headers.get('x-redoc-process-total-time')

        metadata_base64 = response.headers.get('x-redoc-xml-metadata')
        metadata_bytes = base64.b64decode(metadata_base64)
        metadata_json = json.loads(metadata_bytes.decode('utf-8'))

        return {
            'buffer': buffer,
            'transaction_id': transaction_id,
            'total_pages': int(totalPages) if totalPages is not None else 0,
            'total_time': int(totalTime) if totalTime is not None else 0,
            'metadata': metadata_json
        }
