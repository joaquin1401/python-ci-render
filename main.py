from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, esta es una app desplegada con Render y CI aca error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000) # El port=10000 es requerido por Render para apps en Python.
