#-*- encoding=UTF-8 -*-
import pandas as pd
import numpy as np

# Dados das eleições primárias dos EUA
eleicoes = pd.read_csv('./datasets/primary-results.csv')
# print eleicoes.head()

# No aggregate, analisamos a coluna 'votes', aplicando 3 funções
# print eleicoes.groupby('candidate').aggregate({'votes':[min, np.mean, max]})

# Onde Hillary Clinton teve 590502 ?
# print eleicoes[eleicoes['votes']==590502]

# print eleicoes.groupby('candidate').aggregate({'votes':[min, np.mean, max], 'fraction_votes':[min, np.mean, max]})

# print eleicoes[eleicoes['fraction_votes']==1]

# print eleicoes[(eleicoes['fraction_votes']==1) & (eleicoes['candidate']=='Hillary Clinton')][-10:]

def votes_filter(x):
    return x['votes'].sum() > 1000000

# print eleicoes.groupby('state').filter(votes_filter)

# alabama = eleicoes[eleicoes['state_abbreviation']=='AL']
# print alabama['votes'].sum()

# print eleicoes[(eleicoes['state_abbreviation']=='WI') &
#          (eleicoes['candidate']=='Hillary Clinton')]['votes'].sum()

# print eleicoes.groupby(['state_abbreviation', 'candidate'])
# print eleicoes.groupby(['state_abbreviation', 'candidate']).aggregate({'votes':[sum], 'fraction_votes':[sum]})

print eleicoes.groupby(['state', 'party', 'candidate']).aggregate({'votes':[np.sum]}).head(7)
tab = pd.pivot_table(eleicoes, index=['state', 'party', 'candidate'], values=['votes'], aggfunc={'votes':np.sum}).head(7)
print tab

grupo = eleicoes.groupby(['county', 'party'])
print 'type(grupo):', type(grupo)

eleicoes['rank'] = grupo['votes'].rank(ascending=False)
print 'eleicoes["rank"]:', type(eleicoes['rank'])

print eleicoes[eleicoes['county']=='Los Angeles']

grupo = eleicoes.groupby(['state', 'party', 'candidate']).sum()
print grupo.head()

del grupo['fips']
del grupo['fraction_votes']
print grupo.head()

grupo.reset_index(inplace=True)
print grupo.head(10)

grupo['rank'] = grupo.groupby(['state', 'party'])['votes'].rank(ascending=False)
print grupo.head(7)

print pd.pivot_table(grupo, index=['state','party','candidate'],values=['rank','votes']).head()

print grupo[grupo['rank']==1].head()

print grupo[grupo['rank']==1]['candidate'].value_counts()