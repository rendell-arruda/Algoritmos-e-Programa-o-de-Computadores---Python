# exercicios dos textos sugeridos

## exemplo de exercício recursivo com contador regressivo
def countdown(n):
    if n <= 0:                  #condição base
        print("Here we go!")
    else:
        print(n)
        countdown(n-1)          #chamada recursiva

print(countdown(10))

## faça uma funcao que calcula um a soma dos itens de uma lista.

def listaSoma(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
l = [1,3,5,7,9]
print(listaSoma(l))

# faça a mesma coisa acima usando recorrencia

def listaSoma_rec(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0]+ listaSoma_rec(numList[1:])

print(listaSoma_rec([1,3,5,7,9]))

#Escreva uma função que receba como parâmetro de entrada um número inteiro N.
# Ela deve retornar 1 se N for primo ou 0, caso não seja.

def ePrimo(n):
    if n < 1 :
        return 'Erro digite outro numero'
    elif p == 2 :
        return 1
    elif p% 2 == 0:
        return 0
    else:
        raiz = p ** 0.5
        R = 1
        i = 3
        while i <= raiz and R != 0:
            R = P % i
            i += 2
            return R


##Escreva uma função que receba duas listas L1 e L2 como parâmetro de entrada e
# retorne uma lista que seja a interseção de L1 e L2, em que uma lista interseção
# é aquela que contém os elementos que estejam presentes em ambas, L1 e L2.

def Intersecao (L1, L2):
    LR = []                         #define a lista resultante vazia
    for e in L1:                    #percorre L1 do in[icio ao fim
        if e in L2:                 #se o elemente e de L1 estiver em L2
            LR.append(e)            #insere e na lista LR
    return LR                       #retorna LR
lista1= [2,3,4,5]
lista2= [2,5,6,7]

print(Intersecao(lista1,lista2))
##
##Suponha que uma lista está carregada com diversos números inteiros.
# Escreva uma função recursiva que calcule a soma desses valores.
# Para testar essa função, use a lista L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cuja soma resulta = 55.

def SomaLista(l):
    print(l)
    if l == []:
        return 0
    else:
        return l[0] + SomaLista(l[1:])


print('Inicio do Programa')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = SomaLista(l)

print('Lista: ', end="")
print(l)
print("Soma dos elementos de l = {0}".format(S))
print("Fim do programa")

## Problema prático 10.1 - Implemente o método recursivo reverse(), que aceita um
# inteiro não negativo como entrada e exibe os dígitos de n verticalmente,
# começando com o dígito de ordem baixa.

def reverse(n):
    'exibe dígitos de n verticalmente, começando com dígito de baixa ordem'
    if n < 10:               #caso básico: numero de um dígito ex n=3124
        print(n)
    else:                   #n tem pelo menos 2 dígitos
        print(n%10)         #obtem e exibe ultimo dígito de n print(3124%10 = 4)
        reverse(n//10)      #manda o numero exibe recursivamente, em reverso tudo menos o último dígito
                            # n = 321 e volta no loop até ter um dígito

reverse(11)
##Problema Prático 10.2
#Use o pensamento recursivo para implementar a função recursiva saúde()
#que, sobre a entrada inteira n, exibe n strings 'Hip ' seguidos por Hurrah

def GritaHurra(n):
    if n == 0:
        print('Hurrah!!')
    else:                    #n > 0
        print('Hip', end=" ")
        GritaHurra(n-1)

GritaHurra(4)


##Problema Prático 10.3
# No Capítulo 5, implementamos a função fatorial() iterativamente.
# A função fatorial n! tem uma definição recursiva natural:
# Reimplemente a função fatorial() usando a recursão.
# Além disso, estime quantas chamadas à fatorial() são feitas para algum valor de entrada n > 0.

def fatorial(n):
    'retorna o fatorial do inteiro n'

    if n <= 1: #ou poderia ser if n in [0,1]:   #caso básico
        return 1
    else:
        return fatorial(n-1) * n           # etapa recursiva quando n > 1

print(fatorial(3))

##Problema Prático 10.4  - Implemente o método recursivo pattern2(), que aceita um inteiro não negativo como
#entrada e exibe o padrão mostrado a seguir.
# Os padrões para as entradas 0 e 1 são nada e um asterisco, respectivamente:
#>>> pattern2(2)
#*
#**
#*

def pattern2(n):
    'exibe o enésimo padrão'
    if n > 0:
        pattern2(n-1) # exibe a funcao com(n-1)
        print(n * '*')
        pattern2(n-1)

pattern2(3)

##

##
