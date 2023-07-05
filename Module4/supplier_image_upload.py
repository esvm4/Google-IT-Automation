#!/usr/bin/env python3
import requests
import os

dir = os.path.expanduser("~/supplier-data/images/")
url = "http://localhost/upload/"
for file in os.listdir(dir):
    if file.endswith("jpeg"):
        with open(dir + file, "rb") as opened:
            r = requests.post(url, files={"file": opened})

print("Uploaded Images Successfully.")
