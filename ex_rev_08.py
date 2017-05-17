# -*- coding: UTF-8 -*-
def negativo(valor):
    return valor * -1

lista = range(11)
print 'lista:', lista
print 'dupli:', lista * 2
print 'Lista de nros pares ao quadrado',[x*2 for x in lista if x % 2 == 0]
print 'Gerando uma lista de LISTAS'
print '\t',[[s.capitalize(), s.upper(), len(s)] for s in ['um', 'dois', 'tres']]
print 'Gerando uma lista de TUPLAS'
print '\t',[(s.capitalize(), s.upper(), len(s)) for s in ['um', 'dois', 'tres']]
print 'funcdo:', map(negativo, lista)
print 'lambda:', map(lambda x: x*3, lista)
print 'Filtrando os elementos de uma lista, de acordo com um criterio:'

def criterio(x):
    return x >= 0

lista = range(-5, 5)
print 'lista sem filtro, ', lista
print 'lista com filtro, ', filter(criterio, lista)