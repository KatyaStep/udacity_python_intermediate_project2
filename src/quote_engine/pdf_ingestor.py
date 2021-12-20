"""
PDFIngestor class converts pdf file to text file. parses txt file and returns a list of quotes
"""
import subprocess
import tempfile
import os
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.text_ingestor import TextIngestor
from quote_engine.quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor class converts pdf file to text file parses txt file and returns a list of quotes"""

    allowed_extensions = [".pdf"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Can not ingest this file.")

        with tempfile.NamedTemporaryFile(
            suffix=".txt", dir=os.path.dirname(__file__)
        ) as tmp:
            print(f"TemporaryFile {tmp.name}")
            subprocess.call(["pdftotext", path, tmp.name])
            return TextIngestor.parse(tmp.name)
