from flask import Flask

app = Flask(__name__)


@app.route("/ingles")
def saludo():
    return "hola mundo"

@app.route("/japones")
def salud():
    return "konichiwa world"


@app.route("/frances")
def salu():
    return "bonour jour"


@app.route("/portugues")
def sal():
    return "bon dia"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=53)