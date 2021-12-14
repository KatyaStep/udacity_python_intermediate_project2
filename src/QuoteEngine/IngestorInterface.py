from abc import ABC, abstractmethod
from QuoteModel import QuoteModel
import os


class IngestorInterface(ABC):
    """An abstract base class with two methods """

    allowed_extensions = ['.csv', '.txt', '.docx', '.pdf']
    current_file = None

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ A class method "can_ingest" verifies if a file can be parsed"""
        file, extension = os.path.splitext(path)
        cls.current_file = extension
        return extension in cls.allowed_extensions

    @abstractmethod
    def parse(self, path: str) -> list():
        """ An abstract method "parse"  for parsing file content."""
        pass



