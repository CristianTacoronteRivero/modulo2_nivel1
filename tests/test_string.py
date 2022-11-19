"""Tests nivel1.strings
"""
from nivel1.string import minusculas, mayusculas


def test_mayusculas_a_minusculas():
    """Test que comprueba la transformacion de mayusculas a minusculas"""
    assert minusculas("QuE TaL") == "que tal"


def test_minusculas_a_mayusculas():
    """Test que comprueba la transformacion de minusculas a mayusculas"""
    assert mayusculas("QuE TaL") == "QUE TAL"
