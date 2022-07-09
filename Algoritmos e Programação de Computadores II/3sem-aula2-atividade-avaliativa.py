##ATIVIDADE AVALIATIVA
def f(v,i):
    if i == 0:
        return i
    else:
        j = f(v, i-1)
        if v[i]>v[j]:
            return i
        else:
            return j

l = [5,4,6,8,1,12]

print(f(l, len(l)-1))

##
'''
def func(n):
    if n <= 1:
        return 1
    else:
        return n * func(n-1)

print(func(4))

##
def f(n):
    if n < 2:
        return n
    else:
        return f(n-1)+ f(n-2)

print(f(6))'''