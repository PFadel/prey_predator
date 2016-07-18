# encoding utf-8
from utils import multi_tupla, add_two_tuples
from euler import euler


# Euler melhorado
def rk2(function, x0, x1, y, n=1):
    if isinstance(y, tuple):
        return rk2_tuple(function, x0, x1, y, n)
    else:
        return rk2_int(function, x0, x1, y, n)


def rk2_int(function, x0, x1, y, n):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h

        temp = function(x_antigo, y_antigo) + function(
            x_antigo, euler(function, x_antigo, x_novo, y_antigo, n))

        y_novo = y_antigo + 0.5 * h * temp
        x_antigo = x_novo
        y_antigo = y_novo

    return y_novo


def rk2_tuple(function, x0, x1, y, n):
    y_antigo = y
    h = (x1 - x0) / float(n)
    x_antigo = x0
    for i in range(1, n + 1):
        x_novo = x_antigo + h

        temp = add_two_tuples(function(x_antigo, y_antigo),
                              function(x_antigo, euler(function, x_antigo,
                                                       x_novo, y_antigo)))

        y_novo = add_two_tuples(y_antigo, multi_tupla(0.5 * h, (temp)))

        x_antigo = x_novo
        y_antigo = y_novo

    return y_novo
