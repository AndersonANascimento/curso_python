#-*- encoding=UTF-8 -*-
import pandas as pd

# medias = pd.DataFrame([['Maria', 10.0], ['Ana', 8.5], ['Fernanda', 9.5]],
#                       columns=['Nome do Aluno', 'Media anual'])
#
# print medias.shape
#
# print medias
#
# print medias['Media anual']
# print medias['Media anual'].mean()
# print medias['Media anual'].median()
# print medias['Media anual'].iloc[2]
# print medias.iloc[2]['Nome do Aluno']
# print medias.iloc[2]['Media anual']

#import pandas as pd

# Trabalhando com nomes de colunas
estados = pd.DataFrame([
['AC', 'Acre', 'Rio Branco'], ['AL', 'Alagoas', 'Maceió'],['AP', 'Amapá', 'Macapá'],
['AM', 'Amazonas', 'Manaus'],['BA', 'Bahia', 'Salvador'],['CE', 'Ceara', 'Fortaleza'],
['DF', 'Distrito Federal', 'Brasília'],['ES', 'Espírito Santo', 'Vitória'],
['GO', 'Goiás', 'Goiânia'], ['MA', 'Maranhão', 'São Luiz'], ['MT', 'Mato Grosso', 'Cuiabá'],
['MS', 'Mato Grosso do Sul', 'Campo Grande'], ['MG', 'Minas Gerais', 'Belo Horizonte'],
['PA', 'Pará', 'Belém'],['PB', 'Paraíba', 'João Pessoa'],['PR', 'Paraná', 'Curitiba'],
['PE', 'Pernambuco', 'Recife'],['PI', 'Piauí', 'Terezina'],
['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],['RN', 'Rio Grande do Norte', 'Natal'],
['RS', 'Rio Grande do Sul', 'Porto Alegre'],['RO', 'Rondônia', 'Porto Velho'],
['RR', 'Roraima', 'Boa Vista'],['SC', 'Santa Catarina', 'Florianópolis'],
['SP', 'São Paulo', 'São Paulo'],['SE', 'Sergipe', 'Aracajú'],
['TO', 'Tocantins', 'Palmas']], columns=['Sigla', 'Estado', 'Capital'])

# print estados
#
# print estados.index
# print estados['Estado']
#
# print estados.ix[3]
# print estados.iloc[3]
#
# print estados.ix[3:6]
#
# print estados.iloc[3:6]
#
# estados.index = pd.Index(range(10,37))
# print estados
#
estados.index = estados['Sigla']
# print estados
#
# print estados.ix['AM']
#
del estados['Sigla']
# print estados

print estados.head()
print '\n'
# Exercício 32: iloc[0]
print estados.iloc[0]

# Exercício 33: slicing
print '\n', estados.iloc[1:15:2]

# Informações sobre municipíos do Amazonas - Exerc. 20
censo_amazonas = pd.read_excel('./datasets/censo_ibge_amazonas.xls')
censo_amazonas.head()
print censo_amazonas.iloc[:10]
