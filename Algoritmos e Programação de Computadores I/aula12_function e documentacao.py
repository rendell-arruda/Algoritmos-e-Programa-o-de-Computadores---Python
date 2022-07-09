#functions
'''def f(x):
    res = x**2 +1
    return res

print(f(40))'''

# usa-se o '#' para fazer comentario de uma linha ou
"""uma sequencia de  3 ''' aspas para abrir e fechar a sessao de comentários"""

# os comentarios nao sao considerados no help da funcao
# para funcionar é necessario adicionar o comentarios dentro da fç com aspas simples

def f(x):
    'Exemplo de documentação de funcões que será impressa por meio da funcao help'
    res = x **2 + 1
    return res
help(f)