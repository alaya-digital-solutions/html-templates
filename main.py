import pandas as pd
from flask import (Flask, render_template)

# lanzar la aplicación web
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    test = pd.read_csv('data/test.csv')
    equipo = test['equipo']
    id_neumatico = test['id_neumatico']
    remaining_useful_life = test['remanent_useful_life']
    print(equipo, id_neumatico, remaining_useful_life)
    return render_template('index.html',
                           tables={
                               'equipo': equipo,
                               'id_neumatico': id_neumatico,
                               'remaining_useful_life': remaining_useful_life})


if __name__ == '__main__':
    app.debug = True
    app.run()


content = [["CAEX 32", "182388", "10"], ["CAEX 64", "182334", "185"],
           ["CAEX 21", "382334", "52"],
           ["CAEX 41", "482334", "64"],
           ["CAEX 43", "582344", "124"],
           ["CAEX 69", "682367", "158"],
           ["CAEX 74", "882374", "269"]]

content = pd.DataFrame(content, columns=["equipo", "id_neumatico",
                                         "remanent_useful_life"])
test = content.copy()
equipo = test['equipo']
id_neumatico = test['id_neumatico']
remaining_useful_life = test['remanent_useful_life']

tables = {
    'equipo': equipo,
    'id_neumatico': id_neumatico,
    'remaining_useful_life': remaining_useful_life
}

content.to_csv("data/test.csv", index=False)
