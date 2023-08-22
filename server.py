from datetime import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year

    return render_template("index.html", random_number=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    name = name.capitalize()
    name_params = {
        "name": name
    }

    # Get the predicted age
    response = requests.get("https://api.agify.io?", params=name_params)
    age = response.json()['age']

    # Get the predicted gender
    response = requests.get("https://api.genderize.io", params=name_params)
    gender = response.json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/2dbe04c9b494e0ec69b4")
    blog_data = response.json()
    return render_template("blog.html", blogs=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
