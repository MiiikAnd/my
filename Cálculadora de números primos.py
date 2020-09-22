# achar um número primo num range

a = int(input('até qual valor você quer saber os primos?'))
for a in range(a):
    divisao = 0
    for x in range(1,a+1):
        resto = a % x
        # print(a, "/", x, resto)
        if resto == 0:
            divisao = divisao + 1 #Toda vez que a condição der certo
    if divisao == 2:
        print('Número primo encontrado {}'.format(a))
    # else:
    #     print('A bosta do núemro {} não é primo'.format(a))