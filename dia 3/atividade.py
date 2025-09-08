print("Olá, mundo!")
'''
print("Olá, mundo!"
SyntaxError: O erro aconteceu pela falta de fechamento de parenteses
'''

nome = "Miguel"
print(nome)
'''
print(nome)
NameError: O erro aconteceu pela falta de definição da variável
'''


def somar(a: float, b: float) -> float:
    return print(a, b)

resultado = somar(10, 5)
print(resultado)
'''
def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)
TypeError: O erro aconteceu pela tentativa de somar uma string com um inteiro, isso também se deve pela falta de especificação da variável
'''


try:
    def dividir(a: int, b: int) -> int:
        return a / b

    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Tipo de variável inválido")
'''
def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")
zeroDivisionError: Erro que pode acontecer caso o usuário tentar dividir por zero
ValueError: O erro pode acontecer caso o usuário digite float
'''


try:
    dados = {
        "nome": "Isaac ",
        "idade": 25,
        "cidade": "São Paulo"
    }

    chave = input("Digite a chave que deseja acessar: ")
    valor = dados.get(chave, "Chave não identificada")
    print(f"O valor da chave '{chave}' é: {valor}")

except KeyError:
    print("Erro: Chave inexistente")
'''
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")
KeyError: O erro pode acontecer caso o usuário digite uma chave que nao existe
Método get(): Também pode tratar o erro de chave inexistente, mas ele retorna um valor padrão caso a chave nao seja encontrada

'''