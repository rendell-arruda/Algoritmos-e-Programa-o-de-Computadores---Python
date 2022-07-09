'''
#

class Pilha:
    def __init__(self):
        self.data = []

    def push(self,x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def empty(self):
        return len(self.data) > 0

p = Pilha()
q = Pilha()

for i in range (5):
    if i % 2 == 0:
        p.push(i)
    else:
        q.push(i)
while p.empty():
    q.push(p.pop())
while q.empty():
    print(q.pop())
'''
##

class S:
    def __init__(self):
        self.v = []
        self.i = -1

    def push(self,x):
        self.i += 1
        self.v.insert(0,x)

    def pop(self):
        if(not self.empty()):
            self.i -= 1
            return self.v.pop()

    def empty(self):
        return self.i < 0

s = S()

for i in range(10):
    s.push(i)

while not s.empty():
    print(s.pop())

##

class S:
    def __init__(self):
        self.v = []
        self.i = -1

    def push(self,x):
        self.i += 1
        self.v.append(x)

    def pop(self):
        if(not self.empty()):
            self.i -= 1
            return self.v.pop()

    def empty(self):
        return self.i < 0

s = S()

for i in range(10):
    s.push(i)

while not s.empty():
    print(s.pop())