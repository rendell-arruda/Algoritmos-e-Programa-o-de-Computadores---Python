''# ordenacao II - merge_sort


def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio, fim)


def intercala(v, ini, meio, fim):
    L = v[ini:meio + 1]
    R = v[meio + 1: fim + 1]
    L.append(999)  # sentinela
    R.append(999)  # sentinela

    i = 0
    j = 0

    for k in range(ini, fim + 1):
        if L[i] <= R[j]:
            v[k] = L[j]
            i += 1
        else:
            v[k] = R[j]
            j += 1


merge_sort(vetor, 0, len(vetor) + 1)

#quick_sort
def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim

    while i< j:
        while v[i] < pivo:
            i +=1
            while v[j] > pivo
                j -= 1
            if i <= j
                v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
        if > ini:
            quick_sort(v, ini, j):
            if i < fim:
                quick+sort(v,ini, j)

            if i< fim:quick_sort(v,i, fim)

''