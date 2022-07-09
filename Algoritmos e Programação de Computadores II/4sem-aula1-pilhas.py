# exercicio de pilha
##
class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):  # adiciona o valor na lista INSERIR
        self.data.append(x)

    def pop(self):  # remove o ultimo elemento      RETIRAR
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):  # consulta o elemento
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):  # verifica se esta vazia
        return not len(self.data) > 0


p = Pilha()

p.push(4)
p.push(5)
p.push(6)

## mostrar o numero binario de um numero

p = Pilha()

num = 15                    # criou um numero

while num > 0:              # enquanto o resto da divisao nao for 0
    resto = num % 2         # a gente divide por modulo 2 para saber o resto e
    num = num // 2          # a gente continua dividindo por //2 para pegar o valor inteiro
    p.push(resto)           # armazena o valor do resto na pilha

while not p.empty():
    print(p.pop())
