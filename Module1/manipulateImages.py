#!/usr/bin/env python3

from PIL import Image
import os

for filename in os.listdir("."):  # place this script inside images/
    if filename.startswith("ic_"):  # ignore .DS_Store & this file
        with Image.open(filename) as im:
            im.rotate(270).resize((128, 128)).convert("RGB").save(
                "/opt/icons/{}.jpeg".format(os.path.splitext(filename)[0])
            )

print("Covert Images Successfully.")
