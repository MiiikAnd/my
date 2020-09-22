# lista solta
lista = ['peixe', 'gato', 'cão', 'cavalo']
print(lista[0])

for x in lista:#for numa lista
    print(x)

#  lista para soma

listanum = [9, 3, 8, 1, 2, 3, 4, 5, 6, 7]
soma = 0
for s in listanum:
    print(s)
    soma += s
print(soma)

# Soma mais fácil
print(sum(listanum))
# Maior e menor valor
print(max(listanum))
print(min(listanum))
#  Para buscas em strings a busca será alfabética
listaalfa = ['h', 'a', 'e', 'b']
print(max(listaalfa))
print(min(listaalfa))
# da para usar uma fórmula que valida se tem um elemento na lista
listadepets = ['cão', 'ga', 'peixe', 'cavalo']
if 'gato' in listadepets:
    print('Já tem um gato')
else:
    print('não tem um gato')
# da para inclusive incluir os não existentes:
listadepets = ['cão', 'ga', 'peixe', 'cavalo']
if 'gato' in listadepets:
    print('Já tem um gato')
else:
    print('não tem um gato')
    listadepets.append('gato')
    print('gato inserido')
print(listadepets)
# Da para tirar o item da lista com o pop se deixado em branco tira o ultimo da lisca, o número tira na posição
listadepets.pop(1)
print('retirado o item escrito errado, agora está: ', listadepets)
# Da para tirar item da lista com o remove com o nome exato do item da lista
listadepets.remove('peixe')
print('agora a lista perdeu o peixe', listadepets)

#  Listas são multiplicaveis mas apenas repete os valores
lista2 = lista*3
listanum2 = listanum*2
print(lista2, listanum2)
lista2.remove('peixe')
print('teste da lista dois, quantos peixes sairam?', lista2) #sai só um a primeira posição da lista

# Da para ordenar as listas tanto texto quanto numero use sort
listaalfa.sort()
listanum.sort()
print(listaalfa)
print(listanum)
# Da para ordenar as listas tanto texto quanto numero AO CONTRÁRIO use reverse
listanum.reverse()
print(listanum)
print('a lista de números tem tantos elementos:', len(listanum))
#tupla é imutável  !!! e deve ser escrito entre parenteses
testetupla = (1, 2, 3, 4, 5)
print(testetupla)
print(testetupla[3])

# tem como contar os elementos usando o len tanto na lista quanto na tupla
print(len(testetupla))
# é possivel converter listas e elementos em tuplas com o tuple
listanum_tupla = tuple(listanum)
print('o novo tipo agora é tupla', type(listanum_tupla))
print('Veja que agora está com os parenteses e não mais colchetes', listanum_tupla)
# o processo contrário pode ser feito com o comando list
listanum_tupladesfeita = list(listanum_tupla)
print(type(listanum_tupladesfeita), 'veja essa merda que tem até valor entre colchetes \n', listanum_tupladesfeita)


lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)
