'''
# MOTIVACAO PARA DICIONARIOS
#{<chave 1>:<valor 1>, <chave 2>:<valor 2>, ..., <chave i>:<valor i>}
empregado = {
    '864-20-9753': ['Anna', 'Karenina'],
    '987-65-4321': ['Yu', 'Tsun'],
    '100-01-0010': ['Hans', 'Castorp']}

empregado['987-65-4321']

empregado['864-20-9753']

#outro dicionario

dias = {'Seg':'Segunda', 'Ter':'Terça', 'Qua':'Quarta ','Qui':'Quinta'}
dias['Seg']

'''
##
'''
# problema pratico 6.1
#Escreva uma função estadoNasc() que aceite como entrada o nome completo de um presidente dos
# Estados Unidos (como uma string) e retorne o estado em que ele nasceu.
# Você deverá usar esse dicionário para armazenar o estado em que cada presidente recente nasceu:

def estadoNasc(presidente):
    'retorna o estado de nascimento do presidente informado'

    estados = {'Barack Hussein Obama II':'Hawaii',
               'George Walker Bush':'Connecticut',
               'William Jefferson Clinton':'Arkansas',
               'George Herbert Walker Bush':'Massachussetts',
               'Ronald Wilson Reagan':'Illinois',
               'James Earl Carter, Jr':'Georgia'}
    return estados[presidente]

estadoNasc('Barack Hussein Obama II')'''

##
#problema pratico 6.2 - Falta continuar aqui


