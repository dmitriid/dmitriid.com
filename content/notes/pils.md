+++
title = "pils"
draft = true
date = "2016-09-28T13:58:37+02:00"

+++

```python

import os, sys
from PIL import Image, ImageDraw, ImageFont
import urllib2
import textwrap
from image_utils import ImageText

data = urllib2.urlopen("https://farm1.staticflickr.com/98/232243912_950205e71e_b_d.jpg")

file = "/Users/dmitriid/Projects/dmitriid.com/formo/aaa.jpg"

CHUNK = 16*1024

with open(file, 'wb') as f:
  while True:
    chunk = data.read(CHUNK)
    if not chunk: break
    f.write(chunk)

color = (34,34,34)
text = u"In Vino Veritas, или Взгляд дилетанта на вино"
font = "/Users/dmitriid/Downloads/Merriweather/Merriweather-Regular.ttf"

overlay = Image.open(file)
(original_width, original_height) = overlay.size
overlay.thumbnail((800,600), Image.ANTIALIAS)
overlay.save(file + ".png")

img = ImageText((800, 600), background=(241, 237, 234))
(width, height) = img.write_text_box((10,10), text=text, box_width=780, font_filename=font, color=color, font_size=40)

# (width, height) = img.write_text((10, 10), text, font_filename=font, font_size='fill', max_width=700, max_height=500, color=color)

img.save("test.png")

img = img.image
img = img.crop((0, 40, width, height+80))
img.save("test-crop.png")

overlay.paste(img, (10,600 - height - 80 - 80))


overlay.save(file + ".png")

non_banner = ImageText((800, 600), background=(241, 237, 234))
non_banner = non_banner.image
logo = Image.open("static/assets/img/logo.png")
non_banner.paste(logo, (10,10), logo)
non_banner.paste(img, (10,600 - height - 80 - 80))
non_banner.save("non_banner.png")


```
