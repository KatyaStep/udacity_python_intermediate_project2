"""
The class inherits the IngestorInterface.
The class depends on the pandas library to complete the defined,
abstract method signatures to parse DOCX files.
"""

from typing import List
import docx
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """DocxIngestor class parses csv file and returns a list of quotes"""

    allowed_extensions = [".docx"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Can not ingest this file.")

        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.replace('"', "").split(" - ")
                body, author = parse
                cls.quotes.append(QuoteModel(body, author))

        return cls.quotes
