#!/usr/bin/env python3

import reports
import emails
import os
from datetime import date

dir = os.path.expanduser("~/supplier-data/descriptions/")
report = []


def process_data(data):
    for item in data:
        report.append(f"name: {item[0]}<br/>weight: {item[1]}\n")
    return report


text_data = []
for file in os.listdir(dir):
    with open(dir + file, "r") as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()

if __name__ == "__main__":
    summary = process_data(text_data)
    paragraph = "<br/><br/>".join(summary)
    title = f"Processed Update on {date.today().strftime('%B %d, %Y')}\n"
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = f"{os.environ.get('USER')}@example.com"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
