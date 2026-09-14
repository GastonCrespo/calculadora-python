"""Tests para las operaciones matematicas de la calculadora."""

import unittest

from calculadora import dividir, multiplicar, restar, sumar


class TestCalculadora(unittest.TestCase):
    """Casos de prueba para las cuatro operaciones basicas."""

    def test_sumar_numeros_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_sumar_numeros_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 5), 5)

    def test_restar_numeros_positivos(self):
        self.assertEqual(restar(10, 4), 6)

    def test_restar_resultado_negativo(self):
        self.assertEqual(restar(4, 10), -6)

    def test_multiplicar_numeros_positivos(self):
        self.assertEqual(multiplicar(6, 7), 42)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(5, 0), 0)

    def test_multiplicar_resultado_negativo(self):
        self.assertEqual(multiplicar(-4, 3), -12)

    def test_dividir_numeros_positivos(self):
        self.assertEqual(dividir(10, 4), 2.5)

    def test_dividir_numero_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_uno_entre_dos(self):
        self.assertEqual(dividir(1, 2), 0.5)


if __name__ == "__main__":
    unittest.main()