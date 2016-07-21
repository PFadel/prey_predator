# encoding utf-8
import math
from methods.am3 import am3
from methods.rk4 import rk4
from UI import (ask_for_intervals, ask_for_time, ask_for_entry,
                ask_for_function, ask_for_limit)

limit_pop = False
max_preys = 300


def const_function(t, y):
    alfa = 0.4
    beta = 0.01
    delta = 0.2
    gama = 0.001
    preys = y[0]
    predators = y[1]
    if limit_pop is False or predators != 0:
        return (alfa * preys - beta * preys * predators,
                gama * preys * predators - delta * predators)
    else:
        return (alfa * (max_preys - preys),
                gama * preys * predators - delta * predators)


def var_function(t, y):
    alfa = 0.4
    beta = 0.01
    delta = 0.2
    gama = 0.001
    preys = y[0]
    predators = y[1]
    if limit_pop is False or predators != 0:
        return ((2 + math.sin(t)) * alfa * preys - beta * preys * predators,
                gama * preys * predators - delta * predators)
    else:
        return (alfa * (max_preys - preys),
                gama * preys * predators - delta * predators)

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

        entry = ask_for_entry()
        if entry is None:
            print 'Byebye!'
            break

        limit = ask_for_limit()
        if entry is None:
            print 'Byebye!'
            break
        elif limit == 1:
            limit_pop = True
        else:
            limit_pop = False

        choice = ask_for_function()
        if choice is None:
            print 'Byebye!'
            break
        else:
            if choice == 1:
                function = const_function
            elif choice == 2:
                function = var_function

        print 'Resultado: {}'.format(rk4(function, 0, time, entry, intervals))
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

        entry = ask_for_entry()
        if entry is None:
            print 'Byebye!'
            break

        limit = ask_for_limit()
        if entry is None:
            print 'Byebye!'
            break
        elif limit == 1:
            limit_pop = True
        else:
            limit_pop = False

        choice = ask_for_function()
        if choice is None:
            print 'Byebye!'
            break
        else:
            if choice == 1:
                function = const_function
            elif choice == 2:
                function = var_function

        print 'Resultado: {}'.format(am3(function, 0, time, entry, intervals))
        print 'Se deseja sair use [0]!'

    elif method == 0:
        print 'Byebye!'
        break

    else:
        print 'Opcao invalida!'
        print 'Se deseja sair use [0]!'
