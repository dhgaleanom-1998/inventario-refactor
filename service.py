from repository import InventarioRepository
from utils import calcular_estado

class InventarioService:

    def __init__(self):
        self.repo = InventarioRepository()

    def obtener_inventario(self, conexion):

        datos = self.repo.obtener_productos(conexion)

        return [
            {
                "id": d["id"],
                "nombre": d["nombre"],
                "cantidad": d["cantidad"],
                "estado": calcular_estado(d["cantidad"])
            }
            for d in datos
        ]