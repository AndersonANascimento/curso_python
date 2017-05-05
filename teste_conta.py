# -*- coding: UTF-8 -*-

from model import ContaBancaria
#  ou
# import model.ContaBancaria # Não é boa prática

conta = ContaBancaria() # Cria nova instância
conta.agencia = '3715'
conta.numero = '2171-7'
conta.cliente = 'Anderson'
conta.saldo = 1500.0

print 'Cliente:', conta.cliente
print 'Agencia: %s e Conta: %s' % (conta.agencia, conta.numero)
print 'Saldo:', str(conta.saldo)

# Teste dos métodos depositar() e sacar()
conta.depositar(500.0)
if conta.sacar(2500.0):
    print 'Saque realizado com sucesso :)'
else:
    print 'Saldo insuficiente :('

# Teste do método de tranferencia
origem = ContaBancaria()
origem.depositar(1200.0)
destino = ContaBancaria()

print '\nSaldo Inicial Origem:', origem.saldo
print 'Saldo Inicial Destino:', destino.saldo
print 'Transferindo.....'
origem.transferir(500.0,destino)
print 'Saldo Origem:', origem.saldo
print 'Saldo Destino:', destino.saldo
