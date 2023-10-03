# -*- coding: UTF-8 -*-
lista = [50,70,80,40,10,30,20,30]
print("somatorio", sum(lista))
print("frequencia de 30:", lista.count(30))
print("maior elemento:", max(lista))
print("menor elemento:", min(lista))
print("juntando duas lista e formando pares de elementos:")
lista = zip(range(0,5), range(5,10))
print(list(lista))
print("separando os elementos de uma lista de forma itercalada:")
lista = range(0,10)
intercaladas = lista[::2], lista[1::2]
print(lista, "\n", intercaladas)
print("transformando uma lista de strings em uma string CSV:")
lista = ["curso", "de", "data", "sciense", "em", "python"]
csv_values = ";".join(lista)
print(csv_values)