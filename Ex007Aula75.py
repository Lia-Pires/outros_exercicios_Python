from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]


def ordena(item):
  return item['nota']


alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
