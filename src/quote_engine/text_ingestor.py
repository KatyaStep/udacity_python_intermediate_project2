"""
TextIngestor class parses txt file and returns a list of quotes
"""
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel



class TextIngestor(IngestorInterface):
    """TextIngestor class parses txt file and returns a list of quotes"""

    allowed_extensions = [".txt"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f"Can not ingest this file {path}.")

        with open(path, "r", encoding="utf-8-sig") as text_file:
            content = text_file.readlines()
            for line in content:
                sep = " - "
                if sep in line:
                    quote = line.strip().split(sep)
                    body, author = quote
                    cls.quotes.append(QuoteModel(body, author))

        return cls.quotes
