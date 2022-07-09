# exercicio 3.5
# implemente um programa que solicte do usuário uma lista de palavras e depois exiba na tela uma por linha
# todas as strings de quatro letras nessa lista.

lista = ['pare', 'desktop', 'tio', 'pote']
print(lista)
for x in lista:
    if len(x) == 4:
        print(x)
##ou

print('voce ira digitar 4 palavras')
print('--------')
lista = list()
for n in range(1, 5):
    lista.append(input('digite a uma palavra'))

print(lista)
print('relaçao das palavras que possuem 4 letras')
print('-----------')

for x in lista:
    if len(x) == 4:
        print(x)

# u
lista_nomes = []
nome = input('Adicione um nome na lista:')

while nome != '':
    lista_nomes.append(nome)
    nome = input('Adicione um nome na lista:')

print(lista_nomes)

for x in lista_nomes:
    if len(x) == 4:
        print(x)

##exercicio 3.6 Escreva o laço FOR que exibirá as sequência de números a seguir, um por linha, no shell interativo
# do Python.
# a) Inteiros 0 a 9

for numero in range(0, 10):
    print(numero)

# b) Inteiros de 0 a 1
for numero in range(0, 2):
    print(numero)

##exercicio 3.7 - Escreva um laço FOR que exiba a seguinte seguencia de numeros, um por linha
# a) inteiros de 3 até 12, inclusive este.
for numero in range(3, 13):
    print(numero)

# b) inteiros de 0 (não incluso) até 9, com passo de 2 em vez do padrão.
for numero in range(0, 9, 2):
    print(numero)

# c) inteiros de 0 (não incluso) até 24, com passo de 3.
for numero in range(0, 24, 3):
    print(numero)

# d) inteiros de 3 (não incluso) ate 12, com passo de 5.
for numero in range(3, 12, 5):
    print(numero)
'''

# ATIVIDADE AVALIATIVA
#1
'''
frase = 'algoritmos'
for c in frase:
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
        print('Consoante: ', c)

# ou
frase = 'algoritmos'
for c in frase:
    if c not in 'aeiou':
        print('Consoante: ', c)

# 2
for num in range(10, 100 + 1):
    print('O quadrado de: ', num, 'é: ', num ** 2)

# 3
numero = 1
while numero <= 5:
    if (numero == 3):
        numero += 1
        continue
    print(numero)
    numero += 1
print('Fim')

# 4
lista = ['cebola', 1.85, 'tomate', 4.05, 'cenoura', 4.22]
for x in lista:
    print(x)

# 5
import random

sorteio = random.randint(1, 11)
tentativa = 1

while tentativa < 5:
    num = int(input("Adivinhe um numero entre 1 e 10 :"))
    tentativa += 1
    if num == sorteio:
        print('Parabéns, ', num)
        break
    elif num < sorteio:
        print("numero maior")
    else:
        print("numero menor")
print("Tentativas", tentativa - 1)

# 6
num = int(input("numero desejado: "))
fatorial = 1
x = 1
while x <= num:
    fatorial = fatorial * x
    x += 1
print(fatorial)


# ou

def fatorial_calc():
    num = eval(input("Digite o valor desejado: "))
    fatorial = 1
    x = 1

    if num < 0:
        print("Digite o valor maior que zero")
        fatorial_calc()

    else:
        while x <= num:
            fatorial *= x
            x += 1
        print(fatorial)


# 7
reprovado = 0
exame = 0
aprovado = 0

for cont in range(1, 3):
    print('entre com as notas: ', cont)
    nota1 = eval(input('digite not1: '))
    nota2 = eval(input('digite not2: '))
    media = (nota1 + nota2) / 2
    if media <= 5:
        print('Reprovado')
        reprovado = reprovado + 1
    elif media < 7:
        print('Exame: | ')
        exame = exame + 1
    else:
        print('Aprovado')
        aprovado = aprovado + 1
print('total de exame, ', exame)

#contador de letras 'o'

frase = 'Algoritmos e ProgramacãO de Computadores I'
contLetra = 0

for c in frase:
    if c in 'oO':
        print('Vogal', c)
        contLetra += 1
print('Trocar de letra o ou O: ', contLetra)
