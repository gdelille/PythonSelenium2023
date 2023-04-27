import pytest

class Calculadora:
    def __init__(self):
        pass

    def suma(self, num_a: int, num_b: int):
        return num_a + num_b

    def resta(self, num_a: int, num_b: int):
        return num_a - num_b

    def multiplicacion(self, num_a: int, num_b: int):
        return num_a * num_b

    def division(self, num_a: int, num_b: int):
        return num_a // num_b


def test_suma():
    print("This is a test case")
    result = suma(5, 4)
    assert result == 9, "Operación correcta , la suma de 5+4 debe regresar 9"

