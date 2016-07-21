# encoding utf-8
from utils import multi_tuple, add_many_tuples, add_two_tuples
from rk2 import rk2
import csv


def am3(function, x0, x1, y0, n=1):
    if isinstance(y0, tuple):
        return am3_tuple(function, x0, x1, y0, n)
    else:
        return am3_int(function, x0, x1, y0, n)


def am3_tuple(function, x0, x1, y0, n):

    csv_file_prey = open('results_prey.csv', 'w')
    csv_file_predator = open('results_predator.csv', 'w')
    prey_writer = csv.writer(csv_file_prey)
    predator_writer = csv.writer(csv_file_predator)

    h = (x1 - x0) / float(n)
    # Inicializacao
    x_k_minus_one = x0
    y_k_minus_one = y0

    # Primeiro ponto
    x_k = x0 + h
    y_k = rk2(function, x0, x_k, y0, n)

    # Segundo ponto
    x_k_plus_one = x_k + h
    y_k_plus_one = rk2(function, x_k, x_k_plus_one, y_k, n)

    for i in range(1, n + 1):
        # Calcula temporarias para usar na conta
        temp_k_minus_one = multi_tuple(-1 / 12, function(x_k_minus_one,
                                                         y_k_minus_one))

        temp_k = multi_tuple(8 / 12, function(x_k, y_k))

        temp_k_plus_one = multi_tuple(5 / 12, function(x_k_plus_one,
                                                       y_k_plus_one))

        # Calcula novo valor de Y
        new_y = add_two_tuples(y_k, multi_tuple(h, (add_many_tuples(
            temp_k_minus_one, temp_k, temp_k_plus_one))))

        # Atualiza os valores de X
        x_k_minus_one = x_k
        x_k = x_k_plus_one
        x_k_plus_one = x_k_plus_one + h

        # Atualiza os valores de Y
        y_k_minus_one = y_k
        y_k = y_k_plus_one
        y_k_plus_one = new_y

        # Salva nos arquivos csv
        prey_writer.writerow([x_k_plus_one, y_k_plus_one[0]])
        predator_writer.writerow([x_k_plus_one, y_k_plus_one[1]])

    csv_file_prey.close()
    csv_file_predator.close()
    return y_k_plus_one


def am3_int(function, x0, x1, y0, n):
    h = (x1 - x0) / float(n)
    # Inicializacao
    x_k_minus_one = x0
    y_k_minus_one = y0

    # Primeiro ponto
    x_k = x0 + h
    y_k = rk2(function, x0, x_k, y0, n)

    # Segundo ponto
    x_k_plus_one = x_k + h
    y_k_plus_one = rk2(function, x_k, x_k_plus_one, y_k, n)

    for i in range(1, n + 1):
        # Calcula temporarias para usar na conta
        temp_k_minus_one = -1 / 12 * function(x_k_minus_one, y_k_minus_one)
        temp_k = 8 / 12 * function(x_k, y_k)
        temp_k_plus_one = 5 / 12 * function(x_k_plus_one, y_k_plus_one)

        # Calcula novo valor de Y
        new_y = y_k + h * (temp_k_minus_one + temp_k + temp_k_plus_one)

        # Atualiza os valores de X
        x_k_minus_one = x_k
        x_k = x_k_plus_one
        x_k_plus_one = x_k_plus_one + h

        # Atualiza os valores de Y
        y_k_minus_one = y_k
        y_k = y_k_plus_one
        y_k_plus_one = new_y

    return y_k_plus_one
