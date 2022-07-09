# Programação orientada a objetos.
# aula sobre classe e objetos.
# Classe descreve um conjunto de objetos semelhantes.
# Para se ter um Objeto é necessário ter uma classe antes.
# o Objeto é uma instância da Classe criada.

class Point:
    def __init__(self, x=0, y=0):       # ao criar uma classe o metodo init é criado automaticamente
        self.x = x                      # define um atributo x dentro do init da classe
        self.y = y                      # define um atributo x dentro do init da classe

    def setx(self, x):                  # metodo para setar o x
        self.x = x                      # atualização do novo atributo x

    def sety(self, y):                  # metodo para setar o y
        self.y = y                      # atualização do novo atributo y

    def get(self):                      # metodo para retornar o x e y
        return self.x, self.y

    def move(self, offsetx, offsety):   # metodo para mudar/mover as duas coordenadas
        self.x += offsetx               # soma a coordenada x com o novo ponto
        self.y += offsety               # soma a coordenada y com o novo ponto

    def __repr__(self):                 # metodo para retorna uma string representando o objeto
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p = Point()                             #instanciação da classe Point criando um objeto p
print(p)

q = Point(3, 4)
print(q)
