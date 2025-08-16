from flask import Flask

app = Flask(__name__)


@app.post("/ingles")
def saludo():
    return "hello world"

@app.route("/japoness")
def salud():
    return "konichiwa world"


@app.route("/frances")
def salu():
    return "bonour jour"


@app.route("/portugues")
def sal():
    return "bonito dia"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=34)