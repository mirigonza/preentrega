import sqlite3 as sql

DB_PATH =  "c:\\Users\miria\\OneDrive\\Escritorio\\gitinove\\proyecto_final\\database\\blends.db"

#creo la tabla 
def creacionDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE blends (
        [name] TEXT,
        [compuesto] TEXT,
        [valor] INTEGER
    );
    """)
    conn.commit()
    conn.close()

#le doy valores y contenido 
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("blend de flutas", "te verde, manzana, menta", 350),
        ("blend de especias", "te blanco, cardamomo, jengibre", 350),
        ("tisana herbal", "menta, tomillo, manzanilla", 300),
        ("tisana especias", "rooibos, jengibre, pimienta", 300),
    ]
    cursor.executemany("""INSERT INTO blends VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()



if __name__=="__main__":
   creacionDB()
   addValues()