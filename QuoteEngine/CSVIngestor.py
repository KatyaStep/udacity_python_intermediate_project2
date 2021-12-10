from IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        # TODO: add a docstring
        print('hello there.It"s csv parser!')