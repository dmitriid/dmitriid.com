## Generates og and twitter images
## run
##   python utils.py --images=<path to public/gen/social/index.html>


import ConfigParser
import getopt
import io
import os
import sys
import urllib2

from PIL import Image, ImageDraw, ImageFont


# https://gist.github.com/turicas/1455973
class ImageText(object):
    def __init__(self, filename_or_size, mode='RGBA', background=(0, 0, 0, 0),
                 encoding='utf8'):
        if isinstance(filename_or_size, str):
            self.filename = filename_or_size
            self.image = Image.open(self.filename)
            self.size = self.image.size
        elif isinstance(filename_or_size, (list, tuple)):
            self.size = filename_or_size
            self.image = Image.new(mode, self.size, color=background)
            self.filename = None
        self.draw = ImageDraw.Draw(self.image)
        self.encoding = encoding

    def save(self, filename=None):
        self.image.save(filename or self.filename)

    def get_font_size(self, text, font, max_width=None, max_height=None):
        if max_width is None and max_height is None:
            raise ValueError('You need to pass max_width or max_height')
        font_size = 1
        text_size = self.get_text_size(font, font_size, text)
        if (max_width is not None and text_size[0] > max_width) or \
                (max_height is not None and text_size[1] > max_height):
            raise ValueError("Text can't be filled in only (%dpx, %dpx)" % \
                             text_size)
        while True:
            if (max_width is not None and text_size[0] >= max_width) or \
                    (max_height is not None and text_size[1] >= max_height):
                return font_size - 1
            font_size += 1
            text_size = self.get_text_size(font, font_size, text)

    def write_text(self, (x, y), text, font_filename, font_size=11,
                   color=(0, 0, 0), max_width=None, max_height=None):
        if isinstance(text, str):
            text = text.decode(self.encoding)
        if font_size == 'fill' and \
                (max_width is not None or max_height is not None):
            font_size = self.get_font_size(text, font_filename, max_width,
                                           max_height)
        text_size = self.get_text_size(font_filename, font_size, text)
        font = ImageFont.truetype(font_filename, font_size)
        if x == 'center':
            x = (self.size[0] - text_size[0]) / 2
        if y == 'center':
            y = (self.size[1] - text_size[1]) / 2
        self.draw.text((x, y), text, font=font, fill=color)
        return text_size

    def get_text_size(self, font_filename, font_size, text):
        font = ImageFont.truetype(font_filename, font_size)
        return font.getsize(text)

    def write_text_box(self, (x, y), text, box_width, font_filename,
                       font_size=11, color=(0, 0, 0), place='left',
                       justify_last_line=False):
        lines = []
        line = []
        words = text.split()
        for word in words:
            new_line = ' '.join(line + [word])
            size = self.get_text_size(font_filename, font_size, new_line)
            text_height = size[1]
            if size[0] <= box_width:
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        if line:
            lines.append(line)
        lines = [' '.join(line) for line in lines if line]
        height = y
        for index, line in enumerate(lines):
            height += text_height
            if place == 'left':
                self.write_text((x, height), line, font_filename, font_size,
                                color)
            elif place == 'right':
                total_size = self.get_text_size(font_filename, font_size, line)
                x_left = x + box_width - total_size[0]
                self.write_text((x_left, height), line, font_filename,
                                font_size, color)
            elif place == 'center':
                total_size = self.get_text_size(font_filename, font_size, line)
                x_left = int(x + ((box_width - total_size[0]) / 2))
                self.write_text((x_left, height), line, font_filename,
                                font_size, color)
            elif place == 'justify':
                words = line.split()
                if (index == len(lines) - 1 and not justify_last_line) or \
                                len(words) == 1:
                    self.write_text((x, height), line, font_filename, font_size,
                                    color)
                    continue
                line_without_spaces = ''.join(words)
                total_size = self.get_text_size(font_filename, font_size,
                                                line_without_spaces)
                space_width = (box_width - total_size[0]) / (len(words) - 1.0)
                start_x = x
                for word in words[:-1]:
                    self.write_text((start_x, height), word, font_filename,
                                    font_size, color)
                    word_size = self.get_text_size(font_filename, font_size,
                                                   word)
                    start_x += word_size[0] + space_width
                last_word_size = self.get_text_size(font_filename, font_size,
                                                    words[-1])
                last_word_x = x + box_width - last_word_size[0]
                self.write_text((last_word_x, height), words[-1], font_filename,
                                font_size, color)
        return (box_width, height - y)


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "pf", ["public=", "font="])

    public = None
    font = None

    for opt, arg in opts:
        if opt in ("-p", "--public"):
            public = arg
        elif opt in ("-f", "--font"):
            font = arg

    if public is not None and font is not None:
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(public, 'gen/social/index.html'))
        for section in config.sections():
            background_image = None

            print config.get(section, "title")

            if config.has_option(section, 'image'):
                image_path = config.get(section, 'image')
                if image_path[0] == "\"":
                    image_path = image_path[1:-1]

                if image_path[0:4] == 'http':
                    remote = urllib2.urlopen(image_path)
                    file = io.BytesIO(remote.read())
                    background_image = Image.open(file)
                elif image_path[0:1] == '/':
                    background_image = Image.open(
                        os.path.join(public, image_path[1:]))
            else:
                background_image = ImageText((800, 600),
                                             background=(241, 237, 234))
                background_image = background_image.image
                logo = Image.open("static/assets/img/logo.png")
                background_image.paste(logo, (10, 10), logo)

            text = None

            if config.has_option(section, 'title'):
                text = config.get(section, 'title')
                if text[0] == "\"":
                    text = text[1:-1]

            if config.has_option(section, 'summary'):
                text = config.get(section, 'summary')
                if text and text[0] == "\"":
                    text = text[1:-1]

            out = config.get(section, 'out')
            out_path = os.path.join(public, 'assets/img/cards/', out)
            try:
                os.makedirs(os.path.dirname(out_path))
            except:  # Guard against race condition
                continue

            color = (34, 34, 34)
            text = unicode(text, encoding='utf8', errors='replace')

            background_image.thumbnail((800, 600), Image.ANTIALIAS)

            image_text = ImageText((800, 600), background=(241, 237, 234))
            (width, height) = image_text.write_text_box((10, 10), text=text,
                                                        box_width=780,
                                                        font_filename=font,
                                                        color=color,
                                                        font_size=40)

            image_text = image_text.image
            image_text = image_text.crop((0, 40, width, height + 80))

            background_image.paste(image_text, (10, 600 - height - 80 - 80))

            background_image.save(out_path)
