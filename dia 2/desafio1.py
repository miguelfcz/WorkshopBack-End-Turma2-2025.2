import math

def raiz(num):
    raiz =math.sqrt(num)
    return f'A raiz é: {raiz}'

num = int(input('Digite um número: '))
print(raiz(num))