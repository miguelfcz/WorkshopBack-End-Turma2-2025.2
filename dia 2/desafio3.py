import math

class FiguraGeometrica:
    def area_circulo(self, raio):
        area = math.pi * math.pow(raio, 2)
        return f"A area do circulo é: {area}"
    
    def area_triangulo(self, base, altura):
        area = (base * altura) / 2
        return f"A area do triangulo é: {area}"
    
    def hipo_trianguloretangulo(self, cateto1, cateto2):
        hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
        return f"A hipotenusa do triangulo retangulo é: {hipotenusa}"

print("Bem vindo a calculadora: ",
      "\n 1 - Area do circulo",
      "\n 2 - Area do triangulo",
      "\n 3 - Hipotenusa do triangulo retangulo")

resposta = int(input("\nDigite o número do calculo que quer realizar: "))

calculadora = FiguraGeometrica()

match(resposta):
    case 1:
        raio = float(input("Digite o valor do raio: "))
        print(calculadora.area_circulo(raio))

    case 2:
        base = float(input("Digite o valor da base: "))
        altura = float(input("\nDigite o valor da altura: "))
        print(calculadora.area_triangulo(base,altura))

    case 3:
        cateto1 = float(input("Digite o valor de cateto 1: "))
        cateto2 = float(input("\nDigite o valor de cateto 2: "))
        print(calculadora.hipo_trianguloretangulo(cateto1, cateto2))

    case _:
        print("Opção inválida")