from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#defino metodos y class para darle formato y valores a la tabla
class Blends(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    compuesto = db.Column(db.String)
    valor = db.Column(db.Integer)

    def __init__(self, name, compuesto, valor):
        super().__init__()        
        self.name = name
        self.compuesto = compuesto
        self.valor = valor
      

    def __str__(self):
        return "Nombre: {}. Conpuesto: {}. Valor {}." .format(
            self.name,
            self.compuesto,
            self.valor
        )
    
    def serialize(self):
        return{
            "rowid": self.rowid,
            "name": self.name,
            "compuesto": self.compuesto,
            "valor": self.valor
        }