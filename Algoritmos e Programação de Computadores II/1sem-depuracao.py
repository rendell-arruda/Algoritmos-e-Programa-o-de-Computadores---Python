# teste de depuração de programa com exercicio avaliativo da semana 3

def f(n):
    if n < 2:
        return n
    else:
        return f(n-1) + f(n-2)

print(f(6))