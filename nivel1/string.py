"""Clase encargada de realizar operaciones en cadenas
"""


def minusculas(cadena_text: str) -> str:
    """Pasa a minuscula todos los caracteres del string

    :param cadena_text: cadena de texto
    :type cadena_text: str
    :return: cadena de texto en minuscula
    :rtype: str

    >>> from modulo2.string import minusculas
    >>> minusculas("HOLA")
    'hola'
    """
    return cadena_text.lower()


def mayusculas(cadena_text: str) -> str:
    """Pasa a mayuscula todos los caracteres del string

    :param cadena_text: cadena de texto
    :type cadena_text: str
    :return: cadena de texto en mayuscula
    :rtype: str

    >>> from modulo2.string import mayusculas
    >>> mayusculas("hola")
    'HOLA'
    """
    return cadena_text.upper()
