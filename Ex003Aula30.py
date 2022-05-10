nome = input('Digite seu primeiro nome: ')
letras = int(len(nome))

if letras < 4:
    print('Seu nome é curto!')
elif letras >= 5 and letras <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')