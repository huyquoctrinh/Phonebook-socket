import os, sys
from PIL import Image
import glob


size = 128, 128


thumbnail_dir = "./img/thumbnail/"

full_list = glob.glob("./img/full/*")
print(full_list)

for infile in full_list:
    im = Image.open(infile)
    im.thumbnail(size)
    outfile = infile.split("\\")[-1]
    im.save(thumbnail_dir+outfile, "JPEG")