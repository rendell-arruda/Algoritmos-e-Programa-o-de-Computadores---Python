# recursividade das funcoes

def imprime_rec(l, i=0):
    if i < len(l):
        print(l[i])
    imprime_rec(l, i + 1)


l = [2, 3, 4]

imprime_rec(l)

## problema do fatorial

def fat(n):
    if n==0:
        return 1
    else:
        res = n * fat(n-1)
        return res

print(fat(4))

##
##

