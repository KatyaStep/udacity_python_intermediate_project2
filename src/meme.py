"""The Meme Engine Module is responsible for manipulating and drawing text onto images."""
import os
import random
import argparse
from quote_engine.quote_model import QuoteModel
from quote_engine.ingestor import Ingestor
from meme_engine.meme_engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        # if isinstance(path, list):
        #     img = path[0]
        # else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./static')
    path = meme.make_meme(img_path=img, text=quote.body, author=quote.author)

    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tell us a quote")
    parser.add_argument('--path', type=str)
    parser.add_argument('--body', type=str)
    parser.add_argument('--author', type=str)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
