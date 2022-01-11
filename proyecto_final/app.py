from flask import Flask, jsonify, request, render_template
from Models import db, Blends
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\blends.db"
db.init_app(app)

# conecto el html a la api, para que se ejecute el form
@app.route("/")
def home():
    return render_template("index.html")

#conexion con html form para buscar por nombre un blend o tisana
@app.route("/buscarblend", methods=["GET"])
def buscarblend():
    return render_template("buscarblend.html")

# mostramos en formato json los datos inngresados
@app.route("/api/blends", methods=["GET"])
def getBlends():
    try:
        blends = Blends.query.all()
        toreturn = [blends.serialize()for blends in blends]
        return jsonify(toreturn), 200

    except Exception:
        exception("[SERVER]: error")
        return jsonify({"msg": "ha ocurrido un error"}), 500

  
# comienza la union con html
@app.route("/api/addsblends", methods=["POST"])
def addsblends():
    try:
        name = request.form["name"]
        compuesto = request.form["compuesto"]
        valor = request.form["valor"]
        blend = Blends(name, compuesto, int(valor))
        db.session.add(blend)
        db.session.commit()

        return jsonify(blend.serialize()), 200

    except Exception:
        exception("[SERVER]: error en la ruta de addblends. Log:")
        return jsonify({"msg": "algo salio mal"}), 500

# busca un blend o tisana por nombre
@app.route("/api/buscarblend", methods=["POST"])
def buscarblendForm():
    try:
        nameBlend = request.form["name"]

        blend = Blends.query.filter(Blends.name.like(f"%{nameBlend}%")).first()
        if not blend:
            return jsonify({"msg": "no existe el blend"}), 200
        else:
            return jsonify(blend.serialize()), 200
            
    except Exception:
        exception("[SERVER]: error")
        return jsonify({"msg": "ha ocurrido un error"}), 500



if __name__=="__main__":
    app.run(debug=True, port=5000)