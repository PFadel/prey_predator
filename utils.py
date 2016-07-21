# encoding utf-8


def multi_tuple(escalar, tupla):
    return tuple(x * escalar for x in tupla)


def add_many_tuples(*tuplas):
    resp = (0, 0)
    for t in tuplas:
        resp = add_two_tuples(resp, t)
    return resp


def add_two_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def div_tuple(escalar, tupla):
    return tuple(x / float(escalar) for x in tupla)
