import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

hora = input('Digite um horário (0 à 23): ')
if is_number(hora):
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >=18 and hora <= 23:
        print('Boa Noite')
    else:
        print('Horário inválido')
else:
    print('Você não digitou um horário')


