#-*- encoding=UTF-8 -*-
import pandas as pd

# Informações sobre terrenos de Copacabana - Exerc. 19
copacabana = pd.read_csv('copacabana.csv', delimiter=';')
copacabana.head()

# Informações sobre municipíos do Amazonas - Exerc. 20
censo_amazonas = pd.read_csv('censo_ibge_amazonas.xls')
censo_amazonas.head()

# Informações sobre terrenos de Copacabana - Exerc. 21
print copacabana['Quartos'].describe()