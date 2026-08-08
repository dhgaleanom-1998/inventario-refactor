import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
)
""")

productos = [
    ("Teclado", 3, 85000),
    ("Mouse", 10, 45000),
    ("Monitor", 2, 720000),
    ("Impresora", 7, 550000),
    ("Disco SSD", 1, 280000)
]

cursor.executemany(
    "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
    productos
)

conexion.commit()
conexion.close()

print("Base de datos creada con éxito")