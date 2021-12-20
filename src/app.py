
"""The Quote Engine module is responsible for ingesting many types of files that contain quotes.
For our purposes, a quote contains a body and an author:
"""

import random
import os
import traceback
import requests


from flask import Flask, render_template, request
from quote_engine.ingestor import Ingestor
from meme_engine.meme_engine import MemeEngine
from meme import generate_meme


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []

    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except Exception as exc:
            print(exc)
            traceback.print_exc()

    images_path = "./_data/photos/dog/"

    # use os class to find all images within the images images_path directory
    for root, dirs , files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    temp_img = "./static/temp.jpg"

    body = request.form['body']
    author = request.form['author']

    with open(temp_img, 'wb') as file:
        file.write(requests.get(image_url).content)

    path = None

    try:
        path = generate_meme(temp_img, body, author)
        os.unlink(temp_img)
    except Exception as exc:
        print(exc)
        traceback.print_exc()

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
