#-*- encoding=UTF-8 -*-
import pydataset

# Exibir lista dos 757 datasets disponíveis
print pydataset.data()

# Pegar o dataset do Titanic
titanic = pydataset.data('titanic')
# Exibir os primeiros 5
print titanic.head()

