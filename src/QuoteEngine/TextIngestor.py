from IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        # TODO: add a docstring
        print('hello there.It"s txt parser!')
        return []