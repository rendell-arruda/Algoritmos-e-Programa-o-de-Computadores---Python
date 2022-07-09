#aula
l = [1,2,3]
for x in l:
    print(x)
##

pets = ['cão', 'gato', 'coelho']
for i in pets:
    print(i)
##

s = "algoritmos"
for c in s:
    if c in 'aeiou':
        print(c)
##
#         inicio, start, final
for x in range(1,10,2):
    print(x)
## imprime 'a' 'b' e 'c'
lista = ['a', 'b', 'c']
for i in range(len(lista)):
    print(lista[i])


##
#acumuladores - somar parciais ao longo de uma repeticao
acum = 0
for x in range(1, 30):
    if x % 2 == 0:
        acum = acum + x   # da pra usar o += no lugar do ' = acum'
print(acum)

##
str_list = ['João', 'Roberto', 'Rafael']
for nome in str_list:
    for letra in nome:
        if letra in 'aeiou':
            print(letra)


#exercicios
