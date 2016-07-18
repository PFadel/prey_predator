# encoding utf-8
from methods import rk4


def function(t, y):
    alfa = 0.2
    beta = 0.1
    delta = 0.1
    gama = 0.01
    pop_presa = y[0]
    pop_predador = y[1]
    return (alfa * pop_presa - beta * pop_presa * pop_predador,
            gama * pop_presa * pop_predador - delta * pop_predador)


print rk4(function, 0, 1, (200, 40), 100000)
