#inputs para entrada de dados
# o input sempre retorna uma string
nome = input('digite seu nome:')
print(nome)

# eval: para avaliar a entrada numerica que virou string no input
numero = input('informe um numero:')
eval('numero')

# exercicio de conversao de temperatura
c = input('Digite a temperatura em celsius: ')
c_temp = eval(c) # converte a string em number
f = 1.8 * c_temp + 32

print(f, 'graus Fahrenheit')
