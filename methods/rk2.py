# encoding utf-8
from utils import multi_tuple, add_two_tuples
from euler import euler


# Euler melhorado
def rk2(function, x0, x1, y, n=1):
    if isinstance(y, tuple):
        return rk2_tuple(function, x0, x1, y, n)
    else:
        return rk2_int(function, x0, x1, y, n)


def rk2_int(function, x0, x1, y, n):
    old_y = y
    h = (x1 - x0) / float(n)
    old_x = x0
    for i in range(1, n + 1):
        new_x = old_x + h

        temp = function(old_x, old_y) + function(
            old_x, euler(function, old_x, new_x, old_y, n))

        new_y = old_y + 0.5 * h * temp
        old_x = new_x
        old_y = new_y

    return new_y


def rk2_tuple(function, x0, x1, y, n):
    old_y = y
    h = (x1 - x0) / float(n)
    old_x = x0
    for i in range(1, n + 1):
        new_x = old_x + h

        temp = add_two_tuples(function(old_x, old_y),
                              function(old_x, euler(function, old_x,
                                                    new_x, old_y)))

        new_y = add_two_tuples(old_y, multi_tuple(0.5 * h, (temp)))

        old_x = new_x
        old_y = new_y

    return new_y
