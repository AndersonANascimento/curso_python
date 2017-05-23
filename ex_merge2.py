#-*- encoding=UTF-8 -*-
import pandas as pd

notas = pd.DataFrame(
    {
        'nome': ['Maria', 'Sofia'],
        'nota': [8, 9],
    })

print notas

codigos = pd.DataFrame(
    {
        'nome': ['João', 'Pedro', 'Maria'],
        'cod': [1, 2, 3],
    }
)
print codigos

codigos_notas = pd.merge(codigos, notas)
print codigos_notas

print pd.merge(codigos, notas, how='outer')
print pd.merge(codigos, notas, how='left')
print pd.merge(codigos, notas, how='right')
