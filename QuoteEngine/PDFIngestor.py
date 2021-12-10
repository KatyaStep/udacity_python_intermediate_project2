from IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        # TODO: add a docstring
        print('hello there.It"s pdf parser!')