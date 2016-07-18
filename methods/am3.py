# encoding utf-8
from utils import multi_tupla, soma_tuplas, add_two_tuples
from rk2 import rk2


def am3(function, x0, x1, y0, n=1):
    if isinstance(y0, tuple):
        return am3_tuple(function, x0, x1, y0, n)
    else:
        return am3_int(function, x0, x1, y0, n)


def am3_tuple(function, x0, x1, y0, n):
    h = (x1 - x0) / float(n)
    # Inicializacao
    x_k_menos_um = x0
    y_k_menos_um = y0
    # Primeiro ponto
    x_k = x0 + h
    y_k = rk2(function, x0, x_k, y0, 1)
    x_k_mais_um = x_k + h
    y_k_mais_um = rk2(function, x_k, x_k_mais_um, y_k, 1)
    for i in range(1, n + 1):
        # Calcula temporarias para usar na conta
        temp_k_menos_um = multi_tupla(-1 / 12, function(x_k_menos_um,
                                                        y_k_menos_um))

        temp_k = multi_tupla(8 / 12, function(x_k, y_k))

        temp_k_mais_um = multi_tupla(5 / 12, function(x_k_mais_um,
                                                      y_k_mais_um))

        # Calcula novo valor de Y
        y_novo = add_two_tuples(y_k, multi_tupla(h, (soma_tuplas(
            temp_k_menos_um, temp_k, temp_k_mais_um))))

        # Atualiza os valores de X
        x_k_menos_um = x_k
        x_k = x_k_mais_um
        x_k_mais_um = x_k_mais_um + h

        # Atualiza os valores de Y
        y_k_menos_um = y_k
        y_k = y_k_mais_um
        y_k_mais_um = y_novo

    return y_k_mais_um


def am3_int(function, x0, x1, y0, n):
    h = (x1 - x0) / float(n)
    # Inicializacao
    x_k_menos_um = x0
    y_k_menos_um = y0
    # Primeiro ponto
    x_k = x0 + h
    y_k = rk2(function, x0, x_k, y0, 1)
    x_k_mais_um = x_k + h
    y_k_mais_um = rk2(function, x_k, x_k_mais_um, y_k, 1)
    for i in range(1, n + 1):
        # Calcula temporarias para usar na conta
        temp_k_menos_um = -1 / 12 * function(x_k_menos_um, y_k_menos_um)
        temp_k = 8 / 12 * function(x_k, y_k)
        temp_k_mais_um = 5 / 12 * function(x_k_mais_um, y_k_mais_um)

        # Calcula novo valor de Y
        y_novo = y_k + h * (temp_k_menos_um + temp_k + temp_k_mais_um)

        # Atualiza os valores de X
        x_k_menos_um = x_k
        x_k = x_k_mais_um
        x_k_mais_um = x_k_mais_um + h

        # Atualiza os valores de Y
        y_k_menos_um = y_k
        y_k = y_k_mais_um
        y_k_mais_um = y_novo

    return y_k_mais_um
