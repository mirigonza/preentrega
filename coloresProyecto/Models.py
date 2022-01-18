from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Colorsbase(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    extras = db.Column(db.String, nullable=False)

    def __init__(self, color, descripcion, extras):
        super().__init__()        
        self.color = color
        self.descripcion = descripcion
        self.extras = extras
      

    def __str__(self):
        return "Color: {}. Descripcion: {}. Extras: {}." .format(
            self.color,
            self.descripcion,
            self.extras
        )
    
    def serialize(self):
        return{
            "rowid": self.rowid,
            "color": self.color,
            "descripcion": self.descripcion,
            "extras": self.extras
        }


