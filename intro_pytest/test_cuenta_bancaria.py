# Crea un archivo llamado test_cuenta_bancaria.py
# y agrega la clase de CuentaBancaria

import pytest

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        print(f"saldo {self.saldo}")
        return self.saldo


# Crea una clase de prueba llamada TestCuentaBancaria
# Dentro de la clase de prueba, crea dos métodos setup_method y teardown_method
# En el método setup_methd, crea una nueva instancia de la clase CuentaBancaria y guárdala en una variable de instancia.
# En el método teardown_method, no es necesario hacer nada, ya que no hay nada que limpiar después de cada prueba.
# Define tres métodos de prueba test_depositar, test_retirar y test_retirar_insuficiente.
# En cada método de prueba, utiliza la instancia de la cuenta de prueba craeada en el método setup_method.
# En cada método de prueba, utiliza las aserciones de pytest para verificar que las operaciones de depósio y retiro se realizan correctamente
# y que se lanza una excepción si se intenta retirar más de lo que hay en la cuenta.
# Ejecuta las pruebas utilizando pytest y verifica que todas las pruebs pasen correctamente.

class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta = CuentaBancaria("Iñaqui", 100)

    def test_depositar(self):
       # deposito = CuentaBancaria.depositar(100)
        self.cuenta.depositar(100)
        assert self.cuenta.consultar_saldo() == 200, "Se verifica que la operación depósito es correcta."

    def test_retirar(self):
        self.cuenta.retirar(80)
        assert self.cuenta.consultar_saldo() == 20, "Se verifica que la operación retiro es correcta."

    def test_retirar_dos(self):
        self.cuenta.retirar(120)
        assert self.cuenta.consultar_saldo() == 100, "Se verifica que la operación retiro es correcta y no permite retirar más dinero del saldo disponible."

    def test_retirar_insuficiente(self):
        verifica_excepcion = False
        try:
            self.cuenta.retirar(101)
        except:
            verifica_excepcion = True

        assert verifica_excepcion, "Se verifica que se presenta la excepción cuando no existe saldo."

    def teardown_method(self):
        pass