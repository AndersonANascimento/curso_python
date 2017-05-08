# -*- coding: UTF-8 -*-
from model import ContaBancaria

conta = ContaBancaria()
print 'Saldo inicial:', conta.saldo

conta.depositar(1000)
print 'Saldo após depósito:', conta.saldo

conta.sacar(200.0)
print 'Saldo após saque:', conta.saldo

conta.saldo = 500
print 'Saldo final:', conta.saldo
