# exercicio 2.6
palavras =['taco','bola','celeiro','cesta','peteca']
# primeira e ultima palavra
print(min(palavras))
print(max(palavras))

# exercicio 2.7
notas = [9,7,7,10,3,9,6,6,2]

# (a)Uma expressão que avalia para o número de 7 notas.
print(notas.count(7))
# (b)Uma instrução que muda a última nota para 4.
notas.append(4)
print(notas)

# (c)Uma expressão que avalia para a nota mais alta.
print(max(notas))

# (d)Uma instrução que classifica as notas da lista.
print(type(notas))

# (e)Uma expressão que avalia para a média das notas.
media = (sum(notas)/len(notas))
print(media)

#Exercício 2.8
#Em que ordem os operadores nas expressões a seguir são avaliados?

#(a)2 + 3 == 4 or a >= 5

#(b)lst[1] * -3 < -10 == 0
#(c)(lst[1] * -3 < -10) in [0, True]
#(d)2 * 3**2
#(e)4 / 2 in [1, 2, 3]