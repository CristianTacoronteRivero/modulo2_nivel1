"""Clase encargada de realizar operaciones matematicas
"""


def sumar(number_a: float, number_b: float) -> float:
    """Suma de dos numeros

    :param number_a: numero a
    :type number_a: float
    :param number_b: numero b
    :type number_b: float
    :return: suma del numero a y b
    :rtype: float

    >>> from nivel1.math import sumar
    >>> sumar(3, 5.5)
    8.5
    """
    return number_a + number_b


def restar(number_a: float, number_b: float, modulo: bool = False) -> float:
    """Resta de dos numeros

    :param number_a: numero a
    :type number_a: float
    :param number_b: numero b
    :type number_b: float
    :param modulo: True devuelve el valor absoluto de la resta, defaults to False
    :type modulo: bool, optional
    :return: resta del numero a y b
    :rtype: float

    >>> from nivel1.math import restar
    >>> restar(3, 8)
    -5

    >>> from nivel1.math import restar
    >>> restar(3, 8, modulo=True)
    5
    """
    if modulo:
        return abs(number_a - number_b)
    else:
        return number_a - number_b
