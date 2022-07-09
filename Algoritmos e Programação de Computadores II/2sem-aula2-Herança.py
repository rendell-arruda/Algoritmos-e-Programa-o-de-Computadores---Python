# conceits de herança

# definindo um exemplo de lista e escolha de um numero aleatório
import random


class MyList(list):
    def choice(self):
        return random.choice(self)

l = MyList([2,1,3,4])

