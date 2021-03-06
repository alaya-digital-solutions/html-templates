from flask import (Flask, render_template)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", content=[["CAEX 32", "182388", "125"],
                                                  ["CAEX 64", "182334", "185"],
                                                  ["CAEX 21", "182334", "195"],
                                                  ["CAEX 41", "182334", "269"]])


if __name__ == "__main__":
    app.run()


[["CAEX 32", "182388", "125"],
 ["CAEX 64", "182334", "185"],
 ["CAEX 21", "182334", "195"],
 ["CAEX 41", "182334", "269"]]


lista = [["CAEX 32", "182388", "125"], ["CAEX 64", "182334", "185"],
         ["CAEX 21", "182334", "195"],
         ["CAEX 41", "182334", "269"]]
for i, j, k in range(len(lista)):
    print(i, j, k)
