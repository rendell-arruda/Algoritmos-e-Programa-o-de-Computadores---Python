# exercicio 3.5
# implemente um programa que solicte do usuário uma lista de palavras e depois exiba na tela uma por linha
# todas as strings de quatro letras nessa lista.

lista_nomes = ['nome1', 'nom1', 'nome2', 'nom2']

for x in lista_nomes:
    if len(x) == 4:
        print(x)

##ou
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
for i in range(0, 10):
    print(i)

# b) Inteiros de 0 a 1
for i in range(0, 2):
    print(i)

##exercicio 3.7 - Escreva um laço FOR que exiba a seguinte seguencia de numeros, um por linha
# a) inteiros de 3 até 12, inclusive este.
for i in range(3, 13):
    print(i)

# b) inteiros de 0 (não incluso) até 9, com passo de 2 em vez do padrão.


# c) inteiros de 0 (não incluso) até 24, com passo de 3.

# d) inteiros de 3 (não incluso) ate 12, com passo de 5.


# ATIVIDADE AVALIATIVA
# 1

frase = 'algoritmos'


# ou


# 2 - fatorial

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


# 3
import random

sorteio = random.randint(1, 11)
tentativa = 1
while tentativa < 5:
    num = eval(input("Adivinhe um numero entre 1 e 10: "))
    tentativa += 1
    if num == sorteio:
        print("Parabéns você acertou: ", num)
        break
    elif num < sorteio:
        print("Numero sorteado é maior que o digitado")
    else:
        print("numero sorteado é menor que o digitado")

print("Tentativas", tentativa - 1)

# 4 - programa que mostre as consoantes
frase = "algoritmos"

for x in frase:
    for c in x:
        if c not in 'aeiou':
            print(c)

# 5
for num in range(0,101):
    print("O quadrado de: ", num, 'é ', num**2)


# 6


# 7

# 8
reprovado = 0
exame = 0
aprovado = 0

for cont in range(1,3):
    print("Entre com as notas do Aluno nro.: ", cont)
    nota1 = eval(input('Digite a 1a nota: '))
    nota2 = eval(input('Digite a 2a nota: '))
    media = (nota1 + nota2)/2
    print("Média do aluno %.1f " % media)
    if media < 5:
        print("Reprovado :c")
        reprovado = reprovado + 1
    elif media < 7:
        print("Exame :| ")
        exame = exame + 1
    else:
        print("Aprovado ;) ")
        aprovado = aprovado + 1

print("Total de exame: ",exame)