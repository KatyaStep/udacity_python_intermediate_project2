# The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.
# The application must:
* Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
* Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
* Load, manipulate, and save images.
* Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.

# The project contains the following folders and files:
* _data: contains quotes file to parse, photos
* _fonts: contains a font to use for a meme
* _meme_engine: the module with the following responsibilities:
    * Loading of a file from disk. 
    * Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
   * Add a caption to an image (string input) with a body and author to a random location on the image.
* _quote_engine: the module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author.
  * QuoteModel class - encapsulates the body and author of the quote
  * IngestorInterface class - defines two methods 
    * def can_ingest(cls, path)
    * def parse(cls, path:str)
  * Ingestor class that realizes IngestorInterface abstract class and encapsulates helper classes:
    * csv_parser
    * text_parser
    * pdf_parser
    * docx_parser
* _static - a folder that contains a random generated image from a web form
* _templates - templates for a flask application
* file app.py 
  * uses the Quote Engine module and Meme Generator modules to generate a random captioned image. 
  * app.py uses the requests package to fetch an image from a user submitted URL
* file meme.py. - the program takes three OPTIONAL arguments: 
  A string quote body, A string quote author, An image path
      
        * The program returns a path to a generated image.
        * If any argument is not defined, a random selection is used.

* requirements.txt
* tests folder - contains two test, that was written in the beginning of the project. Do not use these test to verify functions of the project.


# How to set up and run the program
* Install all packages from the file requirements.txt 
  
        * pip install -r requirements.txt
    

* For web application
        
        * python3 app.py
 
    * Go to a web page http://127.0.0.1:5000/ 
    * On the web page a user can generate a random meme or create their own by passing url to an image, text and author.
* For running the program from a command line:

        * python3 meme.py  # no arguments
        * python3 meme.py --body 'Hello there!' --author Kate 
        * python3 meme.py --path './_data/photos/dog/xander_1.jpg' --body 'Hey' --author Kate
