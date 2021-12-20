from unittest import TestCase
from quote_engine.ingestor import Ingestor

TEST_CSV_FILE = 'myfile.csv'
TEST_TXT_FILE = 'myfile.txt'
TEST_DOCX_FILE = 'myfile.docx'
TEST_PDF_FILE = 'myfile.pdf'
TEST_RTF_FILE = 'myfile.rtf'


class TestIngestor(TestCase):
    def test_csv_parse(self, path=TEST_CSV_FILE):
        pass

    def test_txt_parse(self, path=TEST_TXT_FILE ):
        pass

    def test_docx_parse(self, path=TEST_DOCX_FILE):
        pass

    def test_pdf_parse(self, path=TEST_PDF_FILE):
        pass

    def test_rtf_parse(self, path=TEST_RTF_FILE):
        pass