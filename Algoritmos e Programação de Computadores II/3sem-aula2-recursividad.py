# encontrar n-ésimo termo de Fibonacci
# resolucao 1 - recursivo
import time


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# resolucao 2 : fib iterativo


def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res


#exemplo fibonacci memoizado

m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1)+ fib_mem(n-2)
        return m[n]



#calcular tempo de execução
n = 15
start = time.time()
print(fib_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))
start = time.time()
print(fib_it(n))
print('Iterative: {} seconds'.format(time.time() - start))
start = time.time()
print(fib_mem(n))
print('Memoization: {} seconds'.format(time.time() - start))

#memoização
'''#exemplo fatorial
m = dict()
def fat(n):
    if n == 0:
        return 1
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = n * fat(n-1)
        return m[n]

'''
