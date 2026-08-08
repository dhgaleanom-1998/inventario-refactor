class InventarioRepository:

    def obtener_productos(self, conexion):
        return conexion.query(
            "SELECT id, nombre, cantidad FROM productos"
        )