# -*- coding: UTF-8 -*-
# Módulo de Data Science - 15/05/2017
from gibi import Gibi, GibiAmericano

# help(GibiAmericano.carregar)

lista = Gibi.carregar('gibis.csv')

if len(lista) > 0:
    representacao = repr(lista[0])
    a = eval(representacao)
    print 'type(a):', type(a)
    print 'repr(a):', repr(a)


    lista1 = GibiAmericano.carregar('gibis.csv')

    print "tamanho: ", len(lista)

    representacao =  lista1[0].__repr__()   # ou print gibi.repr(gibi)

    a = eval(representacao)
    print 'type(a):', type(a)
    print 'repr(a):', repr(a)