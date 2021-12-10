from IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        # TODO: add a docstring
        print('hello there.It"s docx parser!')
