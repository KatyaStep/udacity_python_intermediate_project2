"""
an abstract base class, IngestorInterface, which defines:
    A complete classmethod method to verify
    if the file type is compatible with the ingestor class.
    An abstract method for parsing the file content (i.e., splitting each row)
    and outputting it to a Quote object.
"""

import os
from typing import List
from abc import ABC, abstractmethod
from quote_engine.quote_model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class with two methods"""

    allowed_extensions = []
    quotes = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """A class method  verifies if a file can be parsed"""
        file, extension = os.path.splitext(path)
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """An abstract method "parse"  for parsing a file content."""
