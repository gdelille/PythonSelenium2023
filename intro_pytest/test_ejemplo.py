# utilizar el assert
#Crear un Test Case que evalúe el método es_par() y determine si el resultado es par o impar.
# En el caso de ser impar, se deberá marcar un error.

import pytest

def es_par(num_a: int,num_b: int) -> bool:
    if num_a%2 == 0 and num_b%2 == 0:
        return True
    else:
        return False

#test positivo
def test_verifica_par():
    resultado = es_par(8,4)
    assert resultado, "Prueba donde se verifica que los dos números son pares."

# test negativo
def test_verifica_primer_numero_par():
    resultado = es_par(8,3)
    assert resultado, "Error: se verifica que el segundo número es impar."

def test_verifica_segundo_numero_par():
    resultado = es_par(3,4)
    assert resultado, "Error: se verifica que el primer número es impar."

def test_verifica_numeros_impares():
    resultado = es_par(9,3)
    assert resultado, "Error: se verifica que los números ingresados son impares."
