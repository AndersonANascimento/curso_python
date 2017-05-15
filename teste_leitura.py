# -*- coding: utf-8 -*-

arquivo = open('gibis.csv','r')

for linha in arquivo:
    linha = linha.strip()
    print linha

arquivo.close()