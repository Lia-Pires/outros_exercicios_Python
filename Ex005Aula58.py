def func1():
    return 'Oi'


def func2(funcao):
    return funcao()



variavel = func2(func1)
print(variavel)