"""#aula
def nfat(L):
    n = 0
    fat = 1
    while fat <= L:
        n += 1
        fat *= n
    ##return n-1
    print(n-1)

nfat (20)


##
num = eval(input('Digite um número positivo:'))
while num < 0:
    num = eval(input('Digite um número positivo:'))

"""
##
#pedir para o usuario digitar um valor natural diferente de zero
valor = eval(input('Digite um valor positivo: '))

while valor < 0:
    valor = eval(input('Digite um valor positivo: '))


##
l = []  # initialization da lista vazia
nome = input('Digite um nome: ')
while nome != '':
    l.append(nome)
    nome = input('Digite um nome:')

for i in l:
    print(i)

## loop infinito
# while True:
    # fazer tal instrucao

# para sair do loop digitar: ctrl+C
