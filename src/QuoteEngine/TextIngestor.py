from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        """TextIngestor class parses txt file and returns a list of quotes"""
        with open(path, 'r', encoding='utf-8-sig') as text_file:
            content = text_file.readlines()
            for line in content:
                quote = line.strip().split(' - ')
                body, author = quote
                cls.quotes.append(QuoteModel(body, author))

        return cls.quotes


# TextIngestor.parse(path='DogQuotesTXT.txt')