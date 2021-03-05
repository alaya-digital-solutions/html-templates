from flask import (Flask, redirect, urlfor, render_template)

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html", content="matheus")


if __name__ == "__main__":
    app.run()
