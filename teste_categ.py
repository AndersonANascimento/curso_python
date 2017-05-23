#-*- encoding=UTF-8 -*-
import pandas as pd
import pydataset as pds

titanic = pds.data('titanic')
print titanic.head()

print titanic.columns

print titanic['class'].describe()

print titanic['class'].nbytes

print titanic['class'][:5] == '3rd class'

titanic['class'] = titanic['class'].astype('category')
print titanic['class'].describe()

print titanic['class'].nbytes

print titanic['class'][:5] == '3rd class'
