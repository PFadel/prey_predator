# encoding utf-8
from methods.am3 import am3
# from methods.rk4 import rk4
# from methods.rk2 import rk2
# from methods.euler import euler


def function(t, y):
    alfa = 0.4
    beta = 0.01
    delta = 0.2
    gama = 0.001
    pop_presa = y[0]
    pop_predador = y[1]
    return (alfa * pop_presa - beta * pop_presa * pop_predador,
            gama * pop_presa * pop_predador - delta * pop_predador)

# for x in range(0, 200):
#     print rk4(function, 0, x, (240, 40), (x + 1) * 64)

print am3(function, 0, 1, (200, 40), 1)
