import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")

productos = cursor.fetchall()

print("=== INVENTARIO DE PRODUCTOS ===\n")

for p in productos:
    print(f"ID: {p[0]}")
    print(f"Producto: {p[1]}")
    print(f"Cantidad: {p[2]}")
    print(f"Precio: ${p[3]:,.0f}")
    print("-" * 30)

conexion.close()