# como definir uma árvore
# um nó (BSTNode - de Binary Search Tree Node) de uma arvore

# Os campos left e right são as referências a outros nós, o campo key
# guarda a chave utilizada para identificar o nó e value representa o valor que desejamos armazenar nele.

class BSTNode():
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

#A construção de um nó, com chave 42, sem valor armazenado e sem filhos pode ser feita da seguinte forma:

root = BSTNode(42)
#Se quisermos adicionar filhos ao nó 42, podemos fazer:

#1 root.left = BSTNode(10)
#2 root.right = BSTNode(90)

#Se quisermos adicionar um filho esquerdo ao nó de valor 10, recém criado, podemos fazer:
#root.left.left = BSTNode(2)


##

class BSTNode():
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        """ retorna uma referencia ao nó de chave key"""
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, node):
        '''Adicionando elemento à subárvore'''
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)