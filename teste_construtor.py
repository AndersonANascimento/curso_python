# -*- coding: UTF-8 -*-
from model import ContaBancaria

print 'Construtor COM saldo'
conta = ContaBancaria(1000.0)
print conta.saldo, conta.contador(), ContaBancaria.contador()

print '\nConstrutor SEM saldo'
conta2 = ContaBancaria()
print conta2.saldo, conta2.contador(), ContaBancaria.contador()
