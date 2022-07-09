#exercicios
'''a = eval(input('Digite o lado 1: '))
b = eval(input('Digite o lado 2: '))
c = eval(input('Digite o lado 3: '))
'''
'''maiorLado = 0
if a > maiorLado:
    maiorLado = a
if b > maiorLado:
    maiorLado = b
if c > maiorLado:
    maiorLado = c'''
'''
#outra alternativa
maiorLado = max(a,b,c)

if maiorLado < (a + b + c - maiorLado):
    print('Os lados formam um triângulo!')
    if a == b and b == c and a == c:
        print('Triângulo equilátero ')
    elif a != b and b != c and a!=c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')


else:
    print('Os lados não foram um triangulo!')
'''
##-----------------
def temperatura(t):
    if t>86:
        print('Quente!')
    elif t>32:
        print('Frio')
    else:
        print('Congelando!')
temperatura(87)