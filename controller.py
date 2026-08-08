from service import InventarioService

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
    service = InventarioService()
    return service.obtener_inventario(conexion)

if __name__ == "__main__":
    print(obtener_inventario())