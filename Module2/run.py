#! /usr/bin/env python3

import os
import requests


keys = ["title", "name", "date", "feedback"]
feedback = dict.fromkeys(keys)

dir = "/data/feedback/"
for file in os.listdir(dir):
    if file.endswith(".txt"):
        with open(dir + file) as f:
            lines = [line.strip() for line in f.readlines()]
            for i in range(len(keys)):
                feedback[keys[i]] = lines[i].strip()
            print(feedback)
            response = requests.post("http://35.239.87.72/feedback/", data=feedback)
            if not response.ok:
                raise Exception(
                    f"POST failed! | Status code: {response.status_code} | File: {file}"
                )
            print("Feedback added!\n")
