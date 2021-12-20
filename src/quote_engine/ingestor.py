"""
This class encapsulates all the ingestors to provide one interface
to load any supported file type.
"""

from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.csv_ingestor import CSVIngestor
from quote_engine.text_ingestor import TextIngestor
from quote_engine.pdf_ingestor import PDFIngestor
from quote_engine.docx_ingestor import DocxIngestor
from quote_engine.quote_model import QuoteModel


class Ingestor(IngestorInterface):
    """This class encapsulates all the ingestors to provide one
    interface to load any supported file type.
    """

    importers = [CSVIngestor, TextIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)

        return []
