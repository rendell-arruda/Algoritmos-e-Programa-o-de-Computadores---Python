#aula
'''#questao 02
b = (4+10+8+2)/4
print(b is int(b))

##questao 3
primeiroBimestre= ("Linguagem Programação I", 8, "semanas", "COM110")

primeiroBimestre[0] = "Algoritmos e Linguagem de Computadores I"

segundoBimestre= primeiroBimestre[0:2]

print(segundoBimestre)

##questao 4
def desconto(num):
    valor1 = valor2 - num
    return valor1

valor1 = 100
valor2 = 200
valor3 = desconto(10)

print("c = ", valor1 + valor2 + valor3)

##questao5

estado = input('digite a sigla do estado: ')

numeroCamisetas= eval(input('Digite o numero de camisetas: '))

if estado == 'sp' or numeroCamisetas>=20:
    print('Frete gratis')
elif estado =='ba':
    print("20tao")
elif estado == 'mg':
    print('40tao')
else:
    print('40tao geral')

##questao6
listaAlunos = ['Carlos','Pedro', ]

for i in listaAlunos:
    print(i)
    for j in range(3):
        print(j)
print('fim')

'''

## questao 7
lista = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    lista[i] = eval(input(f'Entre com valores'))

cont = 0
for i in range (len(lista)):
    if lista[i] == 5:
        cont +=1

print(cont)
print(lista)
##

lista = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    lista[i] = eval(input(f'Entre com valores'))

cont =  lista.count(5)
print(cont)
print(lista)

lista = []
for i in range(11):
    item = eval(input('Insira um numero ou de enter para parar: '))
    if(item != ""):
        lista.append(item)
    else:
        break

def somatorio(Lista):
    listaP = []
    for i in Lista:
        if(i>0):
            listP.append(i)
    print('Soma dos positivos: ', sum(listaP))
somatorio(lista)

##
'''
listaVal = []

for i in range(10):
    item = eval(input("Insira um valor:"))
    listaVal.append(item)

soma = 0
for i in listaVal:
    if i >= 0:
        soma = soma + i

print(soma)'''