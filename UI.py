# encoding utf-8


def ask_for_function():
    while True:
        print 'Se deseja sair use [0]!'
        choice = input('Deseja usar a funcao com constantes de fertilidade ou '
                       'com variacao periodica no indice de presas ? '
                       '[1] Constantes [2] Variacao periodica \n')

        if choice == 0:
            return None
        elif choice in [1, 2]:
            break
        else:
            print 'Essa nao e uma opcao valida!'
    return choice


def ask_for_limit():
    while True:
        print 'Se deseja sair use [0]!'
        choice = input('Deseja limitar o numero de presas ? '
                       '[1] Sim [2] Nao \n')

        if choice == 0:
            return None
        elif choice in [1, 2]:
            break
        else:
            print 'Essa nao e uma opcao valida!'
    return choice


def ask_for_time():
    while True:
        print 'Se deseja sair use [0]!'
        steps = input('Partindo do tempo zero, ate quando deseja ir ? \n')

        if steps == 0:
            return None
        elif isinstance(steps, int):
            break
        else:
            print 'Essa nao e uma opcao valida!'
    return steps


def ask_for_intervals():
    while True:
        print 'Se deseja sair use [0]!'
        intervals = input('Quantos intervalos devemos usar ? \n')
        if intervals == 0:
            return None
        elif isinstance(intervals, int):
            break
        else:
            print 'Essa nao e uma opcao valida!'
    return intervals


def ask_for_entry():
    while True:
        print 'Se deseja sair use [0]!'
        preys = input('Qual deve ser a populacao inicial de presas ? \n')
        if preys == 0:
            return None
        elif isinstance(preys, int):
            print 'Se deseja sair use [0]!'
            predators = input('E de predadores ? \n')
            if predators == 0:
                return None
            elif isinstance(predators, int):
                break
            else:
                print 'Essa nao e uma opcao valida!'
        else:
            print 'Essa nao e uma opcao valida!'
    return (preys, predators)
