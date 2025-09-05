import math

def piso(num):
    piso = math.floor(num)
    return f'Piso: {piso}'

def teto(num):
    teto = math.ceil(num)
    return f'Teto: {teto}'

def proximo_int(num):
    prox_int = math.ceil(num)
    return f'Inteiro mais proximo: {prox_int}'

num = float(input('Digite um número: '))

print(piso(num))
print(teto(num))
print(proximo_int(num))