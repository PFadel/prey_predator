# encoding utf-8
from utils import div_tuple, multi_tuple, add_many_tuples, add_two_tuples
import csv


def rk4(function, x0, x1, y0, n=1, varying=False, should_pop_limit=False):
    if isinstance(y0, tuple):
        return rk4_tuple(function, x0, x1, y0, n)
    else:
        return rk4_int(function, x0, x1, y0, n)


def rk4_tuple(function, x0, x1, y0, n):
    csv_file_prey = open('results_prey.csv', 'w')
    csv_file_predator = open('results_predator.csv', 'w')
    prey_writer = csv.writer(csv_file_prey)
    predator_writer = csv.writer(csv_file_predator)

    # Calcula o tamanho do passo em X dependendo do numero de intervalos
    h = (x1 - x0) / float(n)

    old_y = y0
    old_x = x0
    for i in range(1, n + 1):
        k1 = multi_tuple(h, function(old_x, old_y))
        k2 = multi_tuple(h, function(old_x + 0.5 * h,
                                     add_two_tuples(old_y,
                                                    multi_tuple(0.5, k1))))
        k3 = multi_tuple(h, function(old_x + 0.5 * h,
                                     add_two_tuples(old_y,
                                                    multi_tuple(0.5, k2))))
        k4 = multi_tuple(h, function(old_x + h,
                                     add_two_tuples(old_y, k3)))
        new_x = old_x + h
        new_y = add_two_tuples(old_y, div_tuple(6, add_many_tuples(
            k1 + k2 + k2 + k3 + k3 + k4)))

        old_y = new_y
        old_x = new_x
        prey_writer.writerow([new_x, old_y[0]])
        predator_writer.writerow([new_x, old_y[1]])

    csv_file_prey.close()
    csv_file_predator.close()

    return new_y


def rk4_int(function, x0, x1, y0, n):
    # Calcula o tamanho do passo em X dependendo do numero de intervalos
    h = (x1 - x0) / float(n)

    old_y = y0
    old_x = x0
    for i in range(1, n + 1):
        k1 = h * function(old_x, old_y)
        k2 = h * function(old_x + 0.5 * h, old_y + 0.5 * k1)
        k3 = h * function(old_x + 0.5 * h, old_y + 0.5 * k2)
        k4 = h * function(old_x + h, old_y + k3)
        new_x = old_x + h
        new_y = old_y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        old_y = new_y
        old_x = new_x

    return new_y
