class Pdf:
    def __init__(self, data):
        self.buffer = data['buffer']
        self.transaction_id = data['transaction_id']
        self.total_pages = data['total_pages']
        self.total_time = data['total_time']
        self.metadata = data['metadata']

    def to_buffer(self):
        return self.buffer

    def get_transaction_id(self):
        return self.transaction_id

    def get_total_pages(self):
        return self.total_pages

    def get_total_time_ms(self):
        return self.total_time

    def get_metadata(self):
        return self.metadata
