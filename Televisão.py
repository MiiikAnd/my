class Televisao:
    def __init__(self):
        self.ligada = False
        self.volume = 20

    def liga(self):  # Cuidado com a indentação destas definições
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentavolume(self):
        if self.ligada:
            self.volume += 1

    def diminuivolume(self):
        if self.ligada:
            self.volume -= 1


televisao = Televisao()
print(televisao)
print('A TV está ligada? {}'.format(televisao.ligada))
televisao.liga()
print(televisao.ligada)
televisao.liga()
print(televisao.ligada)
televisao.liga()

print(televisao.ligada)
print('O volume está em {}'.format(televisao.volume))
televisao.aumentavolume()
print('O volume está em {}'.format(televisao.volume))
