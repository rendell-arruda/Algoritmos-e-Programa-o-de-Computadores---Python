#exercicios
# Tendo como dados de entrada a altura e o sexo da pessoas, construa um programa em Python que calcule seu peso
#ideal, utilizando as formulas
"""
sexo = input('Digite h para homens e m para mulheres: ')
altura = input('Digite sua altura em metros: ')

if sexo == 'h':
    pesoIdealM =int((72.7*eval(altura))-58)
    print("Você é do sexo Masculino e seu peso ideal é: ", pesoIdealM)

else:
    pesoIdealF = int((6 x22.1*eval(altura))-44.7)
    print("Você é do sexo Feminino e seu peso ideal é: ", pesoIdealF)

##--------------------------------------------"""
# Faça um programa que le duas notas nota1 e nota2 e informe se ele foi aprovado ou não, com média >=5

nota1 = input('Informe sua nota 01:')
nota2 = input('Informe sua nota 02:')
media = 0.4 *eval(nota1)+0.6*eval(nota2)

if media >= 5:
    print(' APROVADO: Parabéns você está acima da média. Sua média foi: ',media)
else:
    print('REPROVADO. Estude um pouco mais. Sua média foi: ',media)