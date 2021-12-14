import pandas as pd
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        """CSVIngestor class parses csv file and returns a list of quotes"""
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            body, author = row
            cls.quotes.append(QuoteModel(body, author))
        return cls.quotes


# CSVIngestor.parse(path='DogQuotesCSV.csv')