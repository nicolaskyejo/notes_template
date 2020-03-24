"""
A script for generating black borders around images found
in the current directory. Does not delete original images.
"""


import os
import glob
from PIL import Image, ImageOps


FOLDER = 'images_with_blackborder'

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

images = glob.glob('*.png')
images.sort(key=os.path.getmtime)
for file in images:
    ImageOps.expand(Image.open(file), border=5, fill='black').save(os.path.join(FOLDER, file))
