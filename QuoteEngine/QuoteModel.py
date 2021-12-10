class QuoteModel():
    def __init__(self, text_body, author):
        self.quote = text_body
        self.author = author

    def __str__(self):
        print(f'{self.quote} - {self.author}')

