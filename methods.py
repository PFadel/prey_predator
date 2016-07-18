# encoding utf-8
from utils import div_tupla, multi_tupla, soma_tuplas, add_two_tuples


# euler melhorado
def rk2(function, x0, x1, y, n):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h
        y_novo = y_antigo + 0.5 * h * (function(x_antigo, y_antigo) + euler(function, x_antigo, x_novo, y_antigo))
        x_antigo = x_novo
        y_antigo = y_novo
    return y_novo


def euler(function, x0, x1, y, n=1):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h
        y_novo = y_antigo + h * function(x_antigo, y_antigo)
        x_antigo = x_novo
        y_antigo = y_novo
    return y_novo


def rk4(function, x0, x1, y0, n):
    y_antigo = y0
    h = (x1 - x0) / float(n)
    x_antigo = x0
    if isinstance(y0, tuple):
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
    else:
        for i in range(1, n + 1):
            k1 = h * function(x_antigo, y_antigo)
            k2 = h * function(x_antigo + 0.5 * h, y_antigo + 0.5 * k1)
            k3 = h * function(x_antigo + 0.5 * h, y_antigo + 0.5 * k2)
            k4 = h * function(x_antigo + h, y_antigo + k3)
            x_novo = x_antigo + h
            y_novo = y_antigo + (k1 + k2 + k2 + k3 + k3 + k4) / 6
            y_antigo = y_novo
            x_antigo = x_novo
    return x_novo, y_novo
