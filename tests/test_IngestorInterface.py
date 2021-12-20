from unittest import TestCase
from quote_engine.ingestor import Ingestor
from quote_engine.ingestor_interface import IngestorInterface


TEST_CSV_FILE = 'myfile.csv'
TEST_TXT_FILE = 'myfile.txt'
TEST_DOCX_FILE = 'myfile.docx'
TEST_PDF_FILE = 'myfile.pdf'
TEST_RTF_FILE = 'myfile.rtf'


class TestIngestor(TestCase):
    def test_csv_can_ingest(self, path=TEST_CSV_FILE):
        self.csv = IngestorInterface.can_ingest(path)
        self.assertEqual(self.csv, True)

    def test_txt_can_ingest(self, path=TEST_TXT_FILE):
        self.csv = IngestorInterface.can_ingest(path)
        self.assertEqual(self.csv, True)

    def test_docx_can_ingest(self, path=TEST_DOCX_FILE):
        self.csv = IngestorInterface.can_ingest(path)
        self.assertEqual(self.csv, True)

    def test_pdf_can_ingest(self, path=TEST_PDF_FILE):
        self.csv = IngestorInterface.can_ingest(path)
        self.assertEqual(self.csv, True)

    def test_rtf_can_ingest(self, path=TEST_RTF_FILE):
        self.csv = IngestorInterface.can_ingest(path)
        self.assertEqual(self.csv, False)
