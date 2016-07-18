# encoding utf-8
from utils import div_tupla, multi_tupla, soma_tuplas, add_two_tuples


def rk4(function, x0, x1, y0, n=1):
    if isinstance(y0, tuple):
        return rk4_tuple(function, x0, x1, y0, n)
    else:
        return rk4_int(function, x0, x1, y0, n)


def rk4_tuple(function, x0, x1, y0, n):
    y_antigo = y0
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        k1 = multi_tupla(h, function(x_antigo, y_antigo))
        k2 = multi_tupla(h, function(x_antigo + 0.5 * h,
                                     add_two_tuples(y_antigo,
                                                    multi_tupla(0.5, k1))))
        k3 = multi_tupla(h, function(x_antigo + 0.5 * h,
                                     add_two_tuples(y_antigo,
                                                    multi_tupla(0.5, k2))))
        k4 = multi_tupla(h, function(x_antigo + h,
                                     add_two_tuples(y_antigo, k3)))
        x_novo = x_antigo + h
        y_novo = add_two_tuples(y_antigo, div_tupla(soma_tuplas(
            k1 + k2 + k2 + k3 + k3 + k4), 6))

        y_antigo = y_novo
        x_antigo = x_novo

    return y_novo


def rk4_int(function, x0, x1, y0, n):
    y_antigo = y0
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        k1 = h * function(x_antigo, y_antigo)
        k2 = h * function(x_antigo + 0.5 * h, y_antigo + 0.5 * k1)
        k3 = h * function(x_antigo + 0.5 * h, y_antigo + 0.5 * k2)
        k4 = h * function(x_antigo + h, y_antigo + k3)
        x_novo = x_antigo + h
        y_novo = y_antigo + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        y_antigo = y_novo
        x_antigo = x_novo

    return y_novo
