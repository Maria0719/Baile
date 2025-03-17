from flask import Flask, render_template, request

app = Flask(__name__)

# Tarifa por hora
TARIFA_HORA = 50000

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        baile = request.form["baile"]
        horas = int(request.form["horas"])
        costo_total = horas * TARIFA_HORA
        return render_template("resultado.html", baile=baile, horas=horas, costo_total=costo_total)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
