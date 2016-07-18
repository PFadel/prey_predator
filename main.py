# encoding utf-8
# import math
from methods.am3 import am3
from methods.rk4 import rk4
from UI import ask_for_intervals, ask_for_time


def function(t, y):
    alfa = 0.4
    beta = 0.01
    delta = 0.2
    gama = 0.001
    pop_presa = y[0]
    pop_predador = y[1]
    return (alfa * pop_presa - beta * pop_presa * pop_predador,
            gama * pop_presa * pop_predador - delta * pop_predador)

print 'Ola! Bem vindo ao programa em Python mais super duper legal de todos!'
print 'Possuimos dois tipos de metodos, Runge Kutta 4 e Adams Moulton 3!'
print 'Ambos solucionam o problema de presa-predador.'

while True:
    method = input('Qual dos dois deseja usar ? [1] RK4 [2] AM3 \n')
    if method == 1:

        time = ask_for_time()
        if time is None:
            print 'Byebye!'
            break

        intervals = ask_for_intervals()
        if intervals is None:
            print 'Byebye!'
            break

        print rk4(function, 0, time, (240, 40), intervals)

        print 'Se deseja sair use [0]!'

    elif method == 2:
        time = ask_for_time()
        if time is None:
            print 'Byebye!'
            break

        intervals = ask_for_intervals()
        if intervals is None:
            print 'Byebye!'
            break

        print am3(function, 0, time, (240, 40), intervals)

        print 'Se deseja sair use [0]!'

    elif method == 0:
        print 'Byebye!'
        break

    else:
        print 'Opcao invalida!'
        print 'Se deseja sair use [0]!'
