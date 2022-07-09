# Problema Prático 8.1
# Acrescente o método getx() à classe Ponto; esse método não aceita entrada e
# retorna a coordenada x do objeto Ponto que chama o método.
#>>> a.getx()
#3

'''
class Point:
    'classe que representa pontos no plano'

    def setx(self, coordx):
        'define coordenada x ao ponto como coordx'
        self.x = coordx

    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy

    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)

    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy

    def getx(self):
        'retorna a coordenada x do objeto Point que chama o método'
        return(self.x)
'''
'''
#Problema Prático 8.2 - definiçao da classe Teste e teste de herança

class Teste:
    versao = 1.02

'''
'''
class Ponto:
    x = -1
    y = -1

p = Ponto()
p.x = 2
p.y = 3

Ponto.x = 1
Ponto.y = 4

print(Ponto.x)

print(p.x)
print(p.y)

print(Ponto.y)'''

class Cachorro:
    def __init__(self, idade):
        self.idade=idade

class Dalmata(Cachorro):
    def __init__(self, idade, pedigree):
        super(Dalmata.self).__init__(idade)
        self.pedigree = pedigree
d = Dalmata(3,True)
print(d.idade, d.pedigree)