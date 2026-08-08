def conectar_db():
    class DB:
        def query(self, sql):
            return [
                {"id": 1, "nombre": "Teclado", "cantidad": 3},
                {"id": 2, "nombre": "Mouse", "cantidad": 10},
                {"id": 3, "nombre": "Monitor", "cantidad": 2},
            ]
    return DB()

def obtener_inventario():
    conexion = conectar_db()
    datos = conexion.query("SELECT * FROM productos")
    lista = []

    for d in datos:
        if d["cantidad"] < 5:
            alerta = "Bajo stock"
        else:
            alerta = "OK"

        lista.append({
            "id": d["id"],
            "nombre": d["nombre"],
            "cantidad": d["cantidad"],
            "estado": alerta
        })

    return lista

if __name__ == "__main__":
    print(obtener_inventario())