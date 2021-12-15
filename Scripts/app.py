import json
data = {"data": {
  "id": 1,
  "name": "Something",
  "colors": ["red", "blue"]
  }
}

import os
import requests
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
import csv
with open('rates.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for i in data[0]['rates']:
        spamwriter.writerow(i.values())

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def test():
    return render_template("test.html", data=data)

