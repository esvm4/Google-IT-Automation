# Qwiklabs Assessment: Scale and convert images using PIL

## Project Problem Statement

To complete this module, you'll need to write a script that processes a bunch of images. It turns out that your company is in the process of updating its website, and a design contractor has been hired to create some new icon graphics for the site. However, the contractor has delivered the final designs and they’re in the wrong format, rotated 90° and too large. You’re unable to get in contact with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch!

So, how will you do this? You'll need to go through a folder full of images and operate with each of them. On each image, you'll use PIL methods like the ones we saw in the examples, and then write the new images in the right place.

If this sounds tricky, don't panic! You've already seen everything you need to do this, and now it's time to put it into practice.

As in the previous courses, the assessment will be done on a Virtual Machine running in the Cloud, thanks to the Qwiklabs infrastructure. You'll only have access to the VM for a limited amount of time, so we recommend that you write the script locally in your computer first, and only start the lab once your script is working correctly.

Good luck, you've got this!

## Introduction

Your company is in the process of updating its website, and they’ve hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You’re not able to get in contact with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch.

## What you’ll do

Use the Python Imaging Library to do the following to a batch of images:

-   Open an image
-   Rotate an image
-   Resize an image
-   Save an image in a specific format in a separate directory

## Script

Download the file

```bash
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

unzip images.zip
```

The images received are in the wrong format:

-   .tiff format
-   Image resolution 192x192 pixel (too large)
-   Rotated 90° anti-clockwise

The images required for the launch should be in this format:

-   .jpeg format
-   Image resolution 128x128 pixel
-   Should be straight

```bash
cd images/
pip3 install pillow # install pillow
nano manipulateImages.py # create python script
chmod +x edit.py # grant exec permission
./manipulateImages.py # run the script
ls /opt/icons # view the updated images
```

To check image properties:

```bash
python3 # use the Python interpreter
from PIL import Image # import Pillow
img = Image.open("/opt/icons/ic_edit_location_black_48dp.jpeg") # open an image of choice
img.format, img.size # print its properties
exit() # exit the Python interpreter
```
