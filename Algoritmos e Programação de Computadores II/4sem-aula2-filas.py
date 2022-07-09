#
class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0

f = Fila()

f.inserir(1)

# exercício: implemente um programa de gerenciamento de duas filas em um banco: prioritaria e normal.
# seu programa devera permitir que pessoas sejam inseridas no fim de cada fila dependendo da idade de cada
# um (acima de 60 anos entra na fila prioritaria). A saída de pessoas da fila deve ocorrer
# da seguinte forma: a cada duas pessoas que saem da fila prioritária, uma sai da fila normal.