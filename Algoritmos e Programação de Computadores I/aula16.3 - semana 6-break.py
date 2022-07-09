"""
#aula
# for var in sequence:
#   if condition:
        #break
    #else:
        #faça tal instrucao
"""


##

def primo(num):  # numeros divisiveis por 1 por ele mesmo
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    return i == num


print(primo(6))

# continue - forca uma condicao

for n in range(2, 100):
    if not primo(n):
        continue
    print(n)

## pass - ele nao faz nada, só ignora a linha