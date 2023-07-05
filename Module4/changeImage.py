#!/usr/bin/env python3

from PIL import Image
import os

dir = "~/supplier-data/images/"
dir = os.path.expanduser(dir)
for filename in os.listdir(dir):
    if filename.endswith("tiff"):
        with Image.open(dir + filename) as im:
            im.resize((600, 400)).convert("RGB").save(
                f"{dir}/{os.path.splitext(filename)[0]}.jpeg"
            )

print("Changed Images Successfully.")
