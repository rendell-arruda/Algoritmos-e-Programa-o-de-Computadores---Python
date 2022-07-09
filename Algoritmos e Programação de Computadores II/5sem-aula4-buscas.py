"""## busca linear

l = [7, 6, 3, 4]
3 in l

l.index(3)


import random


def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio:
        return -1

    if x == l[meio]:
        return meio
    if x < l[meio]:
        return busca_binaria(l, x, inicio, meio - 1)
    if x > l[meio]:
        return busca_binaria(l, x, meio + 1, fim)


l = random.sample(range(100), 20)
l.sort()
busca_binaria(l, 93, 0, 19)
"""

## definir um codigo de busca binaria e recursivo

def busca_binaria(lista, x, inicio, fim):
    if inicio > fim:
        return -1
    else:
        meio = (inicio + fim) // 2

    if x == lista[meio]:
        return meio
    if x < lista[meio]:
        return busca_binaria(lista, x, inicio, meio -1)
    if x > lista[meio]:
        return busca_binaria(lista,x, meio+1, fim)

import random
lista = random.sample(range(100),20)
lista.sort()