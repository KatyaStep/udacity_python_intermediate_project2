from PIL import Image, ImageDraw, ImageFont
import os


class MemeEngine:
    """meme_engine class with the following responsibility:
        - loading a file from disk
        - transform image by resizing to a maximum  width of 500px while maintaining the input aspect ratio
        - Add a caption to an image (string input) with a body and author to a random location on the image.
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """The signature method to make the meme"""
        image = Image.open(img_path)

        ratio = width/float(image.size[0])
        height = int(ratio*float(image.size[1]))
        img = image.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            quote = text + ' ' + author
            draw.text((10, 30), quote, font=font, fill='white')

        path = None

        try:
            path = os.path.join(self.output_dir, 'image.jpg')
            img.save(path)

        except Exception as exc:
            print(str(exc))

        return path

