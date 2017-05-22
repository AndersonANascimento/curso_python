#-*- encoding=UTF-8 -*-
import pandas as pd

# Informações sobre terrenos de Copacabana - Exerc. 19
<<<<<<< HEAD
copacabana = pd.read_csv('./datasets/copacabana.csv', delimiter=';')
copacabana.head()

# Informações sobre municipíos do Amazonas - Exerc. 20
# censo_amazonas = pd.read_csv('censo_ibge_amazonas.xls')
# censo_amazonas.head()

# Informações sobre terrenos de Copacabana - Exerc. 21
print copacabana['Quartos'].describe()

# Exercício 43: séries booleanas
print 'type(copacabana):\n', type(copacabana)

filtro = copacabana['Quartos'] > 5
print 'type(filtro)', type(filtro)

print filtro

print copacabana['Quartos'].value_counts()

serie = copacabana['Quartos'] == 6
print copacabana.loc[serie]

print copacabana.loc[copacabana['Quartos'] >= 5]

resultado =copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
print 'type(resultado)', type(resultado)

copacabana['TOTAL'] = resultado

print copacabana['TOTAL'].describe()
print  copacabana[['AreaConstruida', 'VAL_UNIT', 'TOTAL']][2:20:3]

=======
copacabana = pd.read_csv('copacabana.csv', delimiter=';')
copacabana.head()

# Informações sobre municipíos do Amazonas - Exerc. 20
censo_amazonas = pd.read_csv('censo_ibge_amazonas.xls')
censo_amazonas.head()

# Informações sobre terrenos de Copacabana - Exerc. 21
print copacabana['Quartos'].describe()
>>>>>>> 48baed94f2f899c1516249f4f2e6c54864a5338d
