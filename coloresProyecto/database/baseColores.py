import sqlite3 as sql

DB_PATH =  "c:\\Users\miria\\OneDrive\\Escritorio\\coloresProyecto\\database\\colorsbase.db"

#creo la tabla 
def creacionDBcolors():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE colorsbase (
        [color] TEXT,
        [descripcion] TEXT,
        [extras] TEXT
    );
    """)
    conn.commit()
    conn.close()

#le doy valores y contenido 
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("Rojo", "Nos provee fuerza y vitalidad", "Gemas: rubi. Hierbas, genjibre"),
        ("Naranja", "Nos provee prosperidad y alegria", "Gemas: cornalina. Hierbas: cascara de naranja"),
        ("Amarillo", "Nos probee claridad de pensamientos", "Gemas: citrino. Hierbas: menta"),
        ("Violeta", "Nos provee cambios y conciencia", "Gemas: amatista. Hierbas: lavanda"),
        ("Verde", "Nos provee salud", "Gemas: cuarzo verde. Hierbas: echinacea"),
        ("Azul", "Nos provee calma", "Gemas: Lapizlazuli. Hierbas: tilo"),
        ("Blanco", "Nos provee pueres", "Gemas: Cuarzo cristal. Hierbas: Manzanilla"), 
    ]
    cursor.executemany("""INSERT INTO colorsbase VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()



if __name__=="__main__":
   creacionDBcolors()
   addValues()