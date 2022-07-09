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

p = Pilha()
for i in range(10):
    p.push(i)

while not p.empty():
    print(p.pop())