# encoding utf-8
from utils import multi_tupla, add_two_tuples


def euler(function, x0, x1, y, n=1):
    if isinstance(y, tuple):
        return euler_tuple(function, x0, x1, y, n)
    else:
        return euler_int(function, x0, x1, y, n)


def euler_int(function, x0, x1, y, n):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h
        y_novo = y_antigo + h * function(x_antigo, y_antigo)
        x_antigo = x_novo
        y_antigo = y_novo

    return y_novo


def euler_tuple(function, x0, x1, y, n):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h
        y_novo = add_two_tuples(y_antigo,
                                multi_tupla(h, function(x_antigo, y_antigo)))
        x_antigo = x_novo
        y_antigo = y_novo

    return y_novo
