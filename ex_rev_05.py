# -*- coding: UTF-8 -*-
import random
lista = [50, 70, 80, 40, 10, 30, 20, 30]
print('lista original\n', lista)
random.shuffle(lista)
print('lista embaralhada\n', lista)
print('Pegando um número aleatório da lista:', random.choice(lista))
print('Amostra aleatória de 4 elementos')
print(random.sample(lista, 4))
print('Lista gerada com 10 números aleatórios(entre 0 e 100)')
print(random.sample(range(0, 100), 10))