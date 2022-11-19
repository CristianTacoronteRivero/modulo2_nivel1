"""Tests nivel1.math
"""
from nivel1.math import sumar, restar


def test_suma_positivo_negativo():
    """Test que comprueba la suma de un numero positivo y otro negativo"""
    assert sumar(5, -2) == 3


def test_resta_negativo_negativo():
    """Test que compriueba la resta de un numero negativo y otro negativo"""
    assert restar(-3, -3) == 0
