'''
# aula 1
def g(x):
    x=5
    print(x)
    return x

a = 3

g(a)
print(a)
'''
'''

# aula 02
def readFile(filename):                 #fç para leitura de um texto
    infile = open(filename, 'r')        # abre o texto e define no modo leitura
    content = infile.read()             # recebe o texto lido e transforma numa lista
    infile.close()                      # fecha o arquivo aberto
    wordList = content.split()          # tranforma a lista em palavras com o split
    print(wordList)                     # imprime a lista de palavras.
    return len(wordList), len(content)  # retorna em duas variáveis essas duas informações, respectivamente:
    # o comprimento da lista de palavras e a quantidade de characteres do texto total.


n_words, n_chars = readFile('texto.txt') #pegas as duas informacoes geradas na fç acima.
print(n_words)
print(n_chars)'''

'''
# aula3 Depuração de codigo.

# exercícios práticos
# 3.14 - Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
# Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.

def trocaPU(lista):
    lista[0], lista[-1] = lista[-1], lista[0]


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
print(ingredientes)
trocaPU(ingredientes)
print(ingredientes)
'''
'''
#PROBLEMA PRÁTICO 3.15 - NAO ENTENDI
#Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos mostrados a seguir.
# Use a função jump() do módulo ch3. Você conseguirá obter a imagem desenhada executando.
'''
"""
#Problema Prático 4.8 -
#Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo —
# e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.

def palavras(nomeArquivo):
    'retorna a lista de palavras reais, sem pontuação'
    arquivoEntrada = open(nomeArquivo,'r')
    conteudo = arquivoEntrada.read()
    arquivoEntrada.close()
    tabela = str.maketrans('!,.:;?', 6 * ' ')
    conteudo = conteudo.translate(tabela)
    conteudo = conteudo.lower()
    return conteudo.split()

print(palavras('texto.txt'))"""

#Problema Prático 4.9 -Implemente a função meuGrep(), que toma como entrada duas strings,
# um nome de arquivo e uma string alvo, e exibe cada linha do arquivo que contém a string alvo como uma substring.

def meuGrep(nomearq, alvo):

    'exibe cada linha do arquivo que contém a string alvo'

    arqEntrada = open(nomearq)

    for linha in arqEntrada:

        if alvo in linha:

           print(linha, end='')

meuGrep('texto.txt', 'Aqui')

#Problema Prático 4.10
#Explique o que causa o erro de sintaxe em cada instrução listada anteriormente.
# Depois, escreva uma versão correta de cada instrução Python.

# a)>>> (3+4]
#
# SyntaxError: invalid syntax

# O parêntese esquerdo e o colchete direito não correspondem.
# A expressão intencionada provavelmente é (3+4), avaliada como o inteiro 7, ou [3+4],
# avaliada como uma lista contendo o inteiro 7.

#b)
# >>> if x == 5
#
# SyntaxError: invalid syntax
#
#A coluna está faltando; a expressão correta é if x == 5:




# c )
#>>> print 'hello'
#
# SyntaxError: invalid syntax
#
# print () é uma função e, portanto, deverá ser chamada com parênteses e com os argumentos,
# se houver, dentro deles; a expressão correta é print('hello').


# d)
# >>> lst = [4;5;6]
#
# SyntaxError: invalid syntax
#
# Os objetos em uma lista são separados por vírgulas: lst = [4,5,6] é o correto.

# e)
#>>> for i in range(10):
#print(i)
# SyntaxError: expected an indented block
#
# A(s) instrução(ões) no corpo de um laço for deve(m) ficar recuada(s).
#
# >>> for i in range(3):
#
#         print(i)
