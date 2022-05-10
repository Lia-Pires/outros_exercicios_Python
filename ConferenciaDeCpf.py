CPF = input('Digite um CPF(apenas numeros):')
n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = CPF
n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = int(n0), int(n1), int(n2), int(n3), int(n4), int(n5), int(n6), int(n7), int(n8), int(n9), int(n10)


variavel_1 = (n0 * 10) + (n1 * 9) + (n2 * 8) + (n3 * 7) + (n4 * 6) + (n5 * 5) + (n6 * 4) + (n7 * 3) + (n8 * 2)
teste_1 = 11 - (variavel_1 % 11)
if teste_1 > 9:
    digito_1 = 0
else:
    digito_1 = teste_1

variavel_2 = (n0 * 11) + (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (digito_1 * 2)
digito_2 = 11 - (variavel_2 % 11)

if (n9) == digito_1 and (n10) == digito_2:
    print('CPF válido!')
else:
    print('CPF inválido!')