#-*- encoding=UTF-8 -*-
import pandas as pd

rotina = pd.read_csv('./datasets/rotina.csv', delimiter=';')
print(rotina.head())

print(rotina.columns)
print(rotina.dtypes)

rotina['StartTime'] = pd.to_datetime(rotina['StartTime'], format='%d/%m/%Y %H:%M')
rotina['EndTime'] = pd.to_datetime(rotina['EndTime'], format='%d/%m/%Y %H:%M')
print(rotina.dtypes)

print(rotina.head())

rotina.set_index('StartTime', inplace=True)
print(rotina.head())

# print(rotina['2011']
# print(rotina['2011-12']
# print(rotina['2011-11-28']
# print(rotina['2011-11-28 10']
print(rotina['2011-11-28 10:33':'2011-11-28 13:06'])