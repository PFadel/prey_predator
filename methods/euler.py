# encoding utf-8
from utils import multi_tuple, add_two_tuples


def euler(function, x0, x1, y, n=1):
    if isinstance(y, tuple):
        return euler_tuple(function, x0, x1, y, n)
    else:
        return euler_int(function, x0, x1, y, n)


def euler_int(function, x0, x1, y, n):
    old_y = y
    h = (x1 - x0) / float(n)
    old_x = x0
    for i in range(1, n + 1):
        new_x = old_x + h
        new_y = old_y + h * function(old_x, old_y)
        old_x = new_x
        old_y = new_y

    return new_y


def euler_tuple(function, x0, x1, y, n):
    old_y = y
    h = (x1 - x0) / float(n)
    old_x = x0
    for i in range(1, n + 1):
        new_x = old_x + h
        new_y = add_two_tuples(old_y, multi_tuple(h, function(old_x, old_y)))

        old_x = new_x
        old_y = new_y

    return new_y
