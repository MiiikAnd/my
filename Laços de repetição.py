resultado = 0
for x in range(1, 10):
    if x < 9:
        resultado += 1
        print(resultado)

# a = int(input('Digite a nota do primeiro bimestre'))
# while a > 10:
#     a = int(input('Digite a nota certa! de 0 - 10')) #problema ao usuário digitar duas vezes o numero
# b = int(input('Nota do segundo bimestre:'))
# while b > 10:
#     b = int(input('Digite a nota certa! de 0 - 10'))
# c = int(input('Nota do terceiro bimestre:'))
# while c > 10:
#     c = int(input('Digite a nota certa! de 0 - 10'))
# d = int(input('Nota do quarto bimestre:'))
# while d > 10:
#     d = int(input('Digite a nota certa! de 0 - 10'))
#
# media = (a + b + c + d ) / 4
#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10 :
#     print ('A nota foi de {}'. format(media))
# else:
#     print('Tem merda aí')
#





# while basico
# a = 0
# while a <= 10:
#     print(a)
#     a += 2







# # achar um número primo num range
# a = int(input('até qual valor você quer saber os primos?'))
# for a in range(a):
#     divisao = 0
#     for x in range(1,a+1):
#         resto = a % x
#         # print(a, "/", x, resto)
#         if resto == 0:
#             divisao = divisao + 1 #Toda vez que a condição der certo
#     if divisao == 2:
#         print('Número primo encontrado {}'.format(a))
#     # else:
#     #     print('A bosta do núemro {} não é primo'.format(a))


# Para achar um numero primo digitado
# a = int(input('Digite um número'))
# divisao = 0
# for x in range(1,a+1):
#     resto = a % x
#     # print(a, "/", x, resto)
#     if resto == 0:
#         divisao = divisao + 1 #Toda vez que a condição der certo
# if divisao == 2:
#     print('Essa merda é prima o número digitado é o {}'.format(a))
# else:
#     print('A bosta do núemro {} não é primo'.format(a))



# for x in range(200):
#     print(x)

