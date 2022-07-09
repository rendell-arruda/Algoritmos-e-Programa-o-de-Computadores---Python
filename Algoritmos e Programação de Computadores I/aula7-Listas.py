## listas, tuplas e operadores
l = [1,2,3]
print(l[2])

#na tuplas muda-se o colchete por parentese

l[0]= 4 ##adiciona o elemento 4 na posicao[0]
print(l)

l.append(7) ##adiciona o elemento '7' na lista
print(l)

print(l.count(4)) ## quantos elementos '4' existem na lista

l.insert(4, 9) ## insere o elementos '9' na posicao 4
print(l)

l.pop() ## remove o ultimo e retorna ele
print(l)

l.remove(2) ## remove o elemento especifico
print(l)

l.reverse() ## inverte a ordem da lista
print(l)

l.sort() ## ordena e organiza a lista por ordem alfabética ou numerica
print(l)

## exercícios
palavras = ['taco','bola','celeiro','cesta', 'peteca']

print(min(palavras)) ## retorna o primeiro valor em ordem alfabética

print(max(palavras)) ## retorna o ultimo valor em ordem alfabética

##escreva:
notas = [9,7,7,10,3,9,6,6,2]

##(a)Uma expressão que avalia para o número de 7 notas.
print(notas.count(7))

## (b)Uma instrução que muda a última nota para 4.
notas.append(4)
print(notas)

## (c)Uma expressão que avalia para a nota mais alta.
print(max(notas))

## (d)Uma instrução que classifica as notas da lista.
notas.sort()
print(notas)

## (e)Uma expressão que avalia para a média das notas.
media = (sum(notas)/len(notas))
print(media)