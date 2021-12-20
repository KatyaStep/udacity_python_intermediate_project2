"""
The class inherits the IngestorInterface.
The class depends on the pandas library to complete the defined,
abstract method signatures to parse CSV files.
"""
from typing import List
import pandas as pd
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor class parses csv file and returns a list of quotes"""

    allowed_extensions = [".csv"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Can not ingest this file.")

        data_frame = pd.read_csv(path)

        for index, row in data_frame.iterrows():
            body, author = row
            cls.quotes.append(QuoteModel(body, author))

        return cls.quotes
