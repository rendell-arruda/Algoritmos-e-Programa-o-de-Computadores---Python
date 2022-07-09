# exercise 1 - implementar a funcao bubble sort para organizar uma lista de numeros.
def bubble_sort(v):
    for i in range(len(v) - 1):
        for j in range(len(v) - i - 1):
            if v[j] > v[j + 1]:                 # numeor da esquerda maior que da direita, entao inverte os numeross
                v[j], v[j + 1] = v[j + 1], v[j] # troca de posiçao

# vetor = [24, 48, 37, 12, 57, 86, 66, 33, 92]
# bubble_sort(vetor)

##
# exercise 2 - insertion sort - insere um numero com os elementos em um subconjunto ja ordenado usando
# uma variavel temporaria intermediaria
def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x


vetor = [24, 48, 37, 12, 57, 86, 66, 33, 92]

insertion_sort(vetor)
##
