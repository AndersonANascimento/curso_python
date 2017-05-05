# -*- coding: UTF-8 -*-
from model import ContaBancaria
from model import Cliente

cliente = Cliente()
cliente.nome = 'Anderson'
cliente.cpf = '111.222.333-44'
cliente.email = 'anderson@gmail.com'

conta = ContaBancaria()
conta.saldo = 1000.0
conta.cliente = cliente

print 'Nome:', conta.cliente.nome
print 'CPF:', conta.cliente.cpf
print 'E-mail:', conta.cliente.email
print 'Saldo:', conta.saldo