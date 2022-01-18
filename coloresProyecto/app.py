
from flask import Flask, jsonify, render_template, request
from Models import db, Colorsbase
from logging import exception


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\colorsbase.db"
db.init_app(app)



@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/colores")
def colores():
    return render_template("colores.html")

@app.route("/api/colores")
def getColors():
    try:
        colors = Colorsbase.query.all()
        toReturn = [color.serialize() for color in colors]
        return jsonify(toReturn), 200

    except Exception:
        print("[SERVER]: error")
        exception("[SERVER[")
        return jsonify({"mje": "erro"}), 500


@app.route("/eleccion", methods=["GET"])
def eleccion():     
    return render_template("eleccion.html")

@app.route("/api/eleccion", methods=["POST"])
def eleccionform():
    try:
        eleccionColor = request.form["color"]

        eleccionForm = Colorsbase.query.filter(Colorsbase.color.like(f"%{eleccionColor}%")).first()
        if not eleccionForm:
            return jsonify({"msg": "no existe el color"}), 200
        else:
            return jsonify(eleccionForm.serialize()), 200
            
    except Exception:
        exception("[SERVER]: error")
        return jsonify({"msg": "ha ocurrido un error"}), 500




if __name__=="__main__":
    app.run(debug=True, port=5000)
