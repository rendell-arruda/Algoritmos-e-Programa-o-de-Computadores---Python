#Atividade avaliativa4
# 1)
import math
num = int(input("Digite um número : "))

quadrado = math.pow(num,3) #pow(numero,expoente) - eleva o numero ao expoente.

raiz = math.sqrt(num) #sqrt retorna a raiz quadrada do numero informado

print(f' o numero ao cubo é {quadrado}')

print(f'A raiz quadrada é {raiz:.2f}')

#2)
def leNumero():
    numero = eval(input("Digite um numero: "))
    return numero
print("numeros lidos")

#3) usa-se o help(nomeDaFuncao) para chamar a documentaçao da funcao

#4)
num =eval(input('Digite um número:'))
funcao =input('Digite quadrado ou cubo:')
if funcao == 'quadrado':
    num=num *num
    print(num)
else:
    num=num*num*num
    print(num)


num = eval(input('Digite um número:'))
funcao = input ('Digite quadrado ou cubo:')
if funcao == 'quadrado':
print(calculaQuadrado(num))
else:
print(num* calculaQuadrado(num))