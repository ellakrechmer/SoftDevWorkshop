# Ella Krechmer, Ivan Lam
# SoftDev
# K19 --A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)
with open('key_nasa.txt', 'r') as f:
    key = f.read()


@app.route("/")
def home():
    data = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + key)
    pic = (json.loads(data.read()))["url"]
    return render_template("main.html", img = pic)


if __name__ == "__main__":
    app.debug = True
    app.run()
