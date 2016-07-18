# encoding utf-8


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
