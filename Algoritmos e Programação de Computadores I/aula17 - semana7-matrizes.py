#aula : lista com duas dimensoes:
m = [[1,2,3],[4,5,6],[7,8,9]] # lista

# podemos acessar como colunas
#  [1,2,3]
#  [2,5,8]
#  [3,8,9]

m[0][0] # acessa o primeiro item da primeira lista
# m[i][j] == m[j][i]   verifica se os elementos sao iguais na mesma posicao
#

def simetrica(m):
    nLinhas = len(m)
    nColunas = len(m[0])

    for i in range(nLinhas):
        for j in range (i + 1, nColunas):
            if m[i][j] != m[j][i]:
                return False
    return True

m = [[1,2,2],[2,4,5],[3,5,2]]
print(simetrica(m))
##



# exercicios

# exercicio 4.1 - comece executando a atribuição:
s = '01Mn4567o9'
print(s)
#escreva expressões usando S e o operador de indexação que sejam avaliadas como:
#a) '234'

print(s[2]+s[3]+s[4])


#b) '78'

for i in range(s[7]+s[8]):
    print(i)
##NÃO ENTENDI

## Exercício 4.2 - supondo que a variável PREVISÃO tenha recebido a string
previsao = 'It will be a sunny day today'

#escreva instrucoes Python correspondentes a estas atribuições:
#a) A variavel CONT , a quantidade de ocorrências da string 'day' na string PREVISAO
#b) a variavel 'clima', o índice em que a substring 'sunny' começa
#c) a variavel 'troca' uma copia de 'previsao' na qual cada ocorrencia
#da substring 'sunny' é submetida por 'cloudy'


'''exercicio 5.9 - usamos o padrao de laço aninhado para gerar 
 os pares de indices de coluna e linha e somarmos as
entradas correspondentes:'''
def add20(t1,t2):
'''t1 e t2 são listas 2d com o mesmo numero de linhas e mesmo
numero de colunas de tamanho igual
add20 incrementa cada item t1[i][j] por t2[i][j]'''

nLinhas = len(t1)               #numero de linhas
nColunas = len(t1[0])           #numero de colunas
for i in range(nLinhas):        #para cada indice de linha i
    for j in range(ncolunas):   # para cada indice de coluna j
        t1[i][j] += t2[i][j]