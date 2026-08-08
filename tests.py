from utils import calcular_estado

def test_bajo_stock():
    assert calcular_estado(3) == "Bajo stock"

def test_ok():
    assert calcular_estado(10) == "OK"

if __name__ == "__main__":
    test_bajo_stock()
    test_ok()
    print("Todas las pruebas pasaron correctamente")