#exercicio 3.2
## a) se a idade é maior que 62, exiba 'Voce pode obter beneficios de pensao'
idade = eval(input('Digite sua idade: '))

if idade >= 62:
    print('Você pode obter benefícios de pensão')
else:
    print('Você não tem direito a pensão')

##b) se o nome esta na lista, exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'
jogadores = ['musial', 'aaraon', 'willians', 'gehrig','ruth']
nome = input('Insira o nome do jogador: ')

if nome.lower() in jogadores:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')
else:
    print('Nome do jogador não consta na lista')

##c) se golpes é maior que 10 e defesa é 0, exiba 'voce esta morto'

golpe = eval(input('insira o valor do golpe: '))
defesa = eval(input('insira o valor da defesa: '))

if golpe > 10 and defesa == 0:
    print('Você está morto')

##d) se pelo menos uma das variáveis boolenas norte, sul, leste e oeste for True, exiba 'Posso escapar'.??
listDirecao = ['norte', 'sul', 'leste', 'oeste']
direcao = input('Digite a direção que você deseja ir: ')
if direcao.lower() in listDirecao:
    print('Posso escapar')
else:
    print('Escolha outra direção!')


##Problema 3.3
#a) se o ano é divisivel por 4, exiba 'Pode ser ano bissexto'. Caso contrário, exiba
# 'Definitivamente não é um ano bissexto'
ano = eval(input('Insira um ano: '))

if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')


#b) Se a lista bilhete é igual a lista loteria, exiba 'Voce ganhou'; se nao exiba 'Melhor sorte da proxima vez..."
loteria = ['2','4','55','67','43']
bilhete = []

while len(bilhete) < 5:
    bilhete.append(input('Insira os 5 numeros do seu bilhete: '))

if loteria == bilhete:
    print('Você ganhou')
else:
    print('Melhor sorte da próxima vez...') 

##Problema 3.4 - Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login
#O programa então verifica se a identificação informada pelo usuário está na lista de usuários válidos. Dependendo do
#resultado sua fç exibirá uma msg apropriada. Não importanto o resultado sua fç deve exibir 'Fim' antes de terminar

usuarios = ['joe','sue', 'hani', 'sophie']
usuario = input('digite seu usuário: ')

if usuario.lower() in usuarios:
    print('Login: ', usuario)
    print('Você entrou')
else:
    print('Login: ', usuario)
    print('Usuário desconhecido. Verifique seu usuário e digite novamente')
print('Fim.')


##Problema 5.1 - Implemente a funcao meu IMC() que aceita como entrada a altura de uma pessoa em metros,
# e peso em kilos e calcula o IMC. Sua fç deve exibir a strind Abaixo do peso se imc<18.5, normal se <=18.5,
# e sobrepeso se imc >-25.

peso = eval(input('Insira seu peso em KG: '))
altura = eval(input(('Insira sua altura em metros: ')))

def meuIMC(peso, altura):
    imc = (peso) / (altura ** 2)
    if imc<18.5:
        print('Você está abaixo do peso')
    elif imc <=25:
        print('Você está normal')
    else:
        print('Você está sobrepeso')

meuIMC(peso,altura)