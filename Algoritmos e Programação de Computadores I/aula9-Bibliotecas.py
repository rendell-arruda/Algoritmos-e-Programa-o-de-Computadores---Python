## Biblioteca padrão
## módulo math - para calculos

import math

print(math.sqrt(4)) ## raiz quadrada

print(math.log(8,2)) ## log de 8 na base 2

print(math.ceil(8.2)) ## arredondamento para cima

print(math.floor(8.2)) ## arredondamento para baixo

## módulo fractions - armazena na forma de frações/racionais

import fractions
a = fractions.Fraction(1,2)
b = fractions.Fraction (3,4)
c= a+b
print(c)

##Problema Prático 2.10

##Escreva expressões Python correspondentes ao seguinte:


##(a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
##(b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
import math

import math
a = 2
b = 3
h = math.sqrt((a**2)+(b**2))

print(h)

maior = h >= 5
print(maior)

#(c)A área de um disco com raio a
import math
a = 3
area = (a**2) * math.pi
print(area)

#(d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
# dentro de um círculo com centro (a, b) e raio r?
