import docx
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        """DocxIngestor class parses csv file and returns a list of quotes"""
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.replace('"', "").split(' - ')
                body, author = parse
                cls.quotes.append(QuoteModel(body, author))

        return cls.quotes


# DocxIngestor.parse(path='DogQuotesDOCX.docx')