from IngestorInterface import IngestorInterface
from CSVIngestor import CSVIngestor
from TextIngestor import TextIngestor
from PDFIngestor import PDFIngestor
from DocxIngestor import DocxIngestor
from QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str):
        # print(cls.can_ingest(path))
        # print(cls.current_file)
        if cls.can_ingest(path):
            if cls.current_file == '.csv':
                CSVIngestor.parse(path)
            if cls.current_file == '.txt':
                TextIngestor.parse(path)
            if cls.current_file == '.docx':
                DocxIngestor.parse(path)
            if cls.current_file == '.pdf':
                PDFIngestor.parse(path)
        else:
            print(
                f'You file can not  be processed. Choose a file from these available '
                f'extensions {cls.allowed_extensions}')


Ingestor.parse(path='myfile.csv')
print()
Ingestor.parse(path='myfile.txt')
print()
Ingestor.parse(path='myfile.docx')
print()
Ingestor.parse(path='myfile.pdf')
print()
Ingestor.parse(path='myfile.rtx')

