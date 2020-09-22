# Função é tudo que retorna valor - metodo não retorna método é também chamado de definição ou definition
class Calculadora:

    def soma(self, a, b):  # serve para aproveitar o código e não ficar escrevendo tudo
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b


calcula = Calculadora()
print(type(calcula))
print(calcula.soma(1, 1))
print(calcula.subtracao(2, 10))
print(calcula.multiplicacao(5, 8))
print(calcula.divisao(5, 10))
