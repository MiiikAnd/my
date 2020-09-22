# Função é tudo que retorna valor - metodo não retorna método é também chamado de definição ou definition
class Calculadora:
    def __init__(self, num1, num2, num3):
        self.a = num1
        self.b = num2
        self.c = num3

    def soma(self):  # serve para aproveitar o código e não ficar escrevendo tudo
        return self.a + self.b + self.c

    def subtracao(self):
        return self.a - self.b - self.c

    def multiplicacao(self):
        return self.a * self.b * self.c

    def divisao(self):
        return self.a / self.b / self.c


calcula = Calculadora(2, 4, 6)
print(calcula.a)
print(calcula)
print(calcula.soma())
print(calcula.subtracao())
print(calcula.multiplicacao())
print(calcula.divisao())
