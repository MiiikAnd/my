conjunto = {90, 1, 2, 3, 4, 5, 6, 6, 6, 4, 4} #conjuntos não possuem duplicidade
conjunto.add(9)# da para incluir com add
conjunto.discard(1)# ou remover elementos com discard
print(type(conjunto))
print('não possui duplicidades:', conjunto)

#uniao com union

conjuto2 = {2, 10, 11, 12, 13, 14}
conjuto3 = {2, 915, 15, 16}
conjuntounido = conjunto.union(conjuto2,conjuto3)
print('Todos os valores duplicados são retirados na união também mas não são colocados em ordem \n', conjuntounido)

conjutointersec = conjunto.intersection(conjuto2, conjuto3)
print('só o que tem de igual entre os todos conjuntos listados mas exibindo só do primeiro \n', conjutointersec)

conjuntodiferente = conjunto.difference(conjuto2, conjuto3)
print('só os que não possuem valores em comuns em relação ao primeiro \n', conjuntodiferente)
diferencasimetrica = conjunto.symmetric_difference(conjuto2)
print('com a diferença simetrica é possivel ver o que tem de diferente entre dois e só dois \n {}'.format(diferencasimetrica))

#subset retorna verdadeiro ou falso de acordo com a relação, um valor fora e retorna false, superset faz o contrário
conjuntoa = {1, 2, 3, 4,}
conjuntob = {1, 2, 3, 4, 5, 6, 7, 8, 9}
teste = conjuntob.issubset(conjuntoa)
print(teste)
teste2 = conjuntob.issuperset(conjuntoa)
print(teste2)

# da para tirar o problema da duplicidade das listas [] convertendo para conjunto usando o set
lista = ['ave', 'ave', 'macaco', 'macaco', 'cão']
conjuntolista = set(lista)
print(conjuntolista)
# e da para reconverter depois
print(lista)
lista = list(conjuntolista)
print(lista)
