'''
## Pilhas
# na pilha o ultimo que entra é o primeiro a sair

class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):  # adiciona o elemento no final da pilha/cabeca da lista
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)  # retira o elemento do final da pilha

    def top(self):  # mostra o ultimo a entrar na pilha sem retira-lo
        if len(self.data) > 0:
            return self.data[-1]

    def empyt(self):
        return len(self.data) > 0

    def __repr__(self):
        return str(self.data)


lista = Pilha()


##
# Listas - na lista a o primeiro elemento a entrar é o primeiro a sair

class Fila():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empyt(self):
        return not len(self.data) > 0


# exercicio fila prioritatia

normal = Fila()
prioritaria = Fila()

normal.push(45)
normal.push(46)
normal.push(47)
normal.push(48)
prioritaria.push(80)
prioritaria.push(84)
prioritaria.push(83)
prioritaria.push(63)

cont = 1
while not normal.empyt() and not prioritaria.empyt():
    if cont % 3 == 0:
        print(normal.pop())
    else:
        print(prioritaria.pop())
    cont += 1
while not normal.empyt():
    print(normal.pop())
while not prioritaria.empyt():
    print(prioritaria.pop())

'''
##
class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def empty(self):
        return len(self.data) > 0
