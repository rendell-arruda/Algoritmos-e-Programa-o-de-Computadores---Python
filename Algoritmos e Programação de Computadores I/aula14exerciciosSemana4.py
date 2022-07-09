# exercicios

"""3.1) Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a
# temperatura em graus Celsius usando a fórmula  OK"""

f = float(input('informe a temperatura em Fahrenheit:'))
# temp_f = eval(f)
c = (5 / 9) * (f - 32)
print("A temperatura é :", c, "celsius")

# ----------------------------------------------------------------

"""3.8) Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada
 e retorna a média dos números. OK"""


def media(numero1, numero2):
    'retorna a média de numer1 e numero2 à função média()'
    res = (numero1 + numero2) / 2
    return res


print(media(2, 3.5))

# ----------------------------------------------------------------
"""3.9) Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo)
 e retorna o perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado perímetro.py"""

import math


def perimetro(raio):
    if raio <= 0:
        print('impossível calcular, insira um número maior que zero')
    else:
        res = 2 * raio * math.pi
        print('O perímetro é: ', res)


perimetro(1)

# ----------------------------------------------------------------
"""3.10)Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha,
 os valores negativos na lista. A função não deverá retornar nada."""


def negativos(lst):
    'exibe os números negativos contidos na lista lst à função negativos()'
    for item in lst:
        if item < 0:
            print(item)


negativos([4, 0, -1, -3, 6, -9])

# ----------------------------------------------------------------
"""3.11)Acrescente a docstring retorna a média de x e y à função média() e a docstring exibe os números negativos
 contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando 
 a ferramenta de documentação help()
"""
#ok
# ----------------------------------------------------------------
'''Exercício 3.12 Desenhe um diagrama representando o estado dos nomes e objetos após esta execução: 
>>> a = [5, 6, 7] 
>>> b = a 
>>> a = 3  
# a= 3 e b = [5,6,7]'''
# ?
# ----------------------------------------------------------------
'''Exercício 3.13
Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou instruções que mapeiam o 
primeiro e último valor da lista. Assim, se a lista original for: 
>>> time = ['Ava','Eleanor','Clare', 'Sarah'] então a lista resultante deverá ser: 
>>> time ['Sarah','Eleanor','Clare','Ava'] '''

time = ['Ava', 'Eleonor', 'Clare', 'Sarah']
print(time[0])  # viu o primeiro item da lista original

print(time[len(time) - 1])  # viu o ultimo item da lista original

time.sort()  # organizou a lista por ordem alfabética
print(time)

time.reverse()  # inverteu a lista organizada
print(time)

# ----------------------------------------------------------------
"""Exercício 3.14
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. 
Você pode considerar que a lista não estará vazia. A função não deverá retornar nada. 

 >>> ingredientes = ['farinha','açúcar','manteiga','maçãs'] 
>>> trocaPU(ingredientes) 
>>> ingredientes 
['maçãs','açúcar','manteiga','farinha'] """

ingredientes = ['farinha', 'açucar', 'manteiga', 'maças']


def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)


trocaPU(ingredientes)
