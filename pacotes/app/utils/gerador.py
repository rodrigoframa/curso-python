from random import randrange, choice

NOMES = ('Rodrigo', 'Camila', 'Ane')


def novo_nome2():
    return NOMES[randrange(3)]


def novo_nome():
    return choice(NOMES)
