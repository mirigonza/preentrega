import sqlite3 as sql 

DB_COLORS = "C:\\Users\\miria\\OneDrive\\Escritorio\\coloresProyecto\\database\\colorsbase.db"


def creacionColors():
    conn = sql.connect(DB_COLORS)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE colors (
        color text,
        descripcion text,
        extras text
    )""" )
    conn.commit()
    conn.close()


def colorsValues():
    conn = sql.connect(DB_COLORS)
    cursor = conn.cursor()
    data = [
        ("Rojo", "Nos provee fuerza y vitalidad", "Gemas: rubi. Hierbas, genjibre")
        ("Naranja", "Nos provee prosperidad y alegria", "Gemas: cornalina. Hierbas: cascara de naranja")
        ("Amarillo", "Nos probee claridad de pensamientos", "Gemas: citrino. Hierbas: menta")
        ("Violeta", "Nos provee cambios y conciencia", "Gemas: amatista. Hierbas: lavanda")
        ("Verde", "Nos provee salud", "Gemas: cuarzo verde. Hierbas: echinacea")
        ("Azul", "Nos provee calma", "Gemas: Lapizlazuli. Hierbas: tilo")
    ]
    cursor.executemany("""INSERT INTO colors VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()



if __name__=="__main__":
    creacionColors()
    colorsValues()

    