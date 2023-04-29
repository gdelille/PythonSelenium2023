# Crea un archivo llamado "test_calculator.py".
# Importa la biblioteca pytest al principio del archivo.
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

# PRUEBAS POSITIVAS
# Crea una función llamada test_suma que use la función suma de la calculadora para sumar dos números
# y verificar que el resultado es correcto utilizando la aserción assert
def test_suma( ):
    print("Este es un caso de prueba para suma")
    calculadora = Calculadora( )
    resultado = calculadora.suma(5, 4)
    assert resultado == 9, "Se verifica que la operación suma se realiza de manera correcta."

# Crea otra función llamada test_resta que use la función resta de la calculadora para restar dos números
# y verificar que el resultado es correcto utilizando la aserción assert
def test_resta( ):
    print("Este es un caso de prueba para resta")
    calculadora = Calculadora( )
    resultado = calculadora.resta(5, 4)
    assert resultado == 1, "Se verifica que la operación resta se realiza de manera correcta."

# Crea una tercera función llamada test_multiplicacion que use la función multiplicacion de la calculadora para multiplicar dos números
# y verificar que el resultado es correcto utilizando la aserción assert
def test_multiplicacion( ):
    print("Este es un caso de prueba para multiplicación")
    calculadora = Calculadora( )
    resultado = calculadora.multiplicacion(5, 4)
    assert resultado == 20, "Se verifica que la operación multiplicación se realiza de manera correcta."

# Crea una cuarta función llamada test_division que use la función division de la calculadora para dividir dos números
# y verificar que el resultado es correcto utilizando la aserción assert
def test_division( ):
    print("Este es un caso de prueba para división")
    calculadora = Calculadora( )
    resultado = calculadora.division(8, 4)
    assert resultado == 2, "Se verifica que la operación división se realiza de manera correcta."
