#! /usr/bin/env python3

import os
import requests
import json

keys = ["name", "weight", "description", "image_name"]
fruit = dict.fromkeys(keys)


dir = os.path.expanduser("~/supplier-data/descriptions/")

for file in os.listdir(dir):
    if file.endswith(".txt"):
        with open(dir + file) as f:
            lines = [line.strip() for line in f.readlines()]
            for i in range(len(keys) - 1):
                fruit[keys[i]] = lines[i].strip()
            weight = fruit["weight"]
            if weight:
                fruit["weight"] = int(weight.strip(" lbs"))
            fruit["image_name"] = file.strip(".txt") + ".jpeg"
            response = requests.post(
                "http://[linux-instance external IP address]/fruits/", data=fruit
            )
            if not response.ok:
                raise Exception(
                    f"POST failed! | Status code: {response.status_code} | File: {file}"
                )
            print("Fruit added!\n")
