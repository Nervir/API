import requests
import csv
from flask import Flask, render_template, request
app = Flask(__name__)

data = {"data": {
  "id": 1,
  "name": "Something",
  "colors": ["red", "blue"]
  }
}


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('rates.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for i in data[0]['rates']:
        spamwriter.writerow(i.values())

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods = ['GET'])
def test():
    if request.method == 'GET':
        return render_template("test.html", data=data)


@app.route("/home", methods = ['POST'])
def home():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        code = request.form['code']
        rates = data[0]['rates']
        for rate in rates:
            if rate['code'].lower() == code.lower():
                bid = rate['bid']
                break
        try:
            if not bid:
                pass
        except UnboundLocalError:
            return "<div> This currency doesn't exist </div>"
        cost = amount * bid
        return render_template("test.html", data=data, cost=cost)


if __name__ == "__main__":
    app.run(debug=True)