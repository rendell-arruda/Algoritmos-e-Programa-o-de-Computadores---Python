'''
#Funções:

#exemplo1
def quadrado(x):
    y = x * x #pode-se excluir a variável y e utilizar o return
    return y

aQuadrar = 10

resultado = quadrado(aQuadrar)
print("O resultado de", aQuadrar, "ao quadrado é", resultado)


### melhoria
def quadrado(x):
    return x*x

aQuadrar = 5

resultado = quadrado(aQuadrar)
print("O resultado de", aQuadrar, "ao quadrado é", resultado)
##


#exemplo2

def quadradoruim(x):
    y = x ** expoente
    return y

expoente = 2
resultado = quadradoruim(10)
print(resultado)


#melhoria

def quadrado_ruim (x, p):
    return x ** p


resultado = quadrado_ruim(10, 2)
print(resultado)

'''

'''
# varredura com WHILE e FOR
# percorrer um range e imprimir os numeros, excluindo o ultimo
for um_valor in range(10):
    print(um_valor)


# percorrer uma string e imprimir os caracteres - iteração por item
for um_chair in "Venha para a festa":
    print(um_chair)


#varredura com for por índice
fruta = "apple"
for idx in range(5):
    currentChar = fruta[idx]
    print(currentChar)



fruta = "apple"
for idx in range(len(fruta)):
    print(fruta[idx])


#imprimir os caracteres das posições pares
str = "python rocks"
for idx in range(len(str)):
    if idx % 2 == 0 :
        print(str[idx])


##Varredura com WHILE
fruta = "apple"
position = 0
while position < len(fruta):
    print(fruta[position])
    position +=1
'''

#acumulação com strings
#exemplo remover vogais

def removeVogal(s):
    vogais = "aeiouAEIOU"
    sSemVogais = ""
    for cadaChar in s:
        if cadaChar not in vogais:
            sSemVogais = sSemVogais + cadaChar
    return sSemVogais

print(removeVogal("rendell"))
print(removeVogal("toda forma"))