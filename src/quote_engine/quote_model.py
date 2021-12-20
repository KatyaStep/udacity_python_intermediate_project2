"""
The class h contains text fields for body and author.
    The class overrides the correct methods to instantiate
    the class and print the model contents as:
    ”body text” - author
"""


class QuoteModel:
    """The class h contains text fields for body and author.
    The class overrides the correct methods to instantiate
    the class and print the model contents as:
    ”body text” - author
    """

    def __init__(self, text_body, author):
        self.body = text_body
        self.author = author

    def __str__(self):
        return f"{self.body} - {self.author}"

    def __repr__(self):
        return f"{self.body} - {self.author}"
