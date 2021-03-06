# -*- coding: UTF-8 -*-

from model import SaldoInsuficienteError, ContaBancaria
#  ou
# import model.ContaBancaria # Não é boa prática

conta = ContaBancaria() # Cria nova instância
conta.agencia = '3715'
conta.numero = '2171-7'
conta.cliente = 'Anderson'
conta.saldo = 1500.0

print type(ContaBancaria), type(conta)
print 'Cliente:', conta.cliente
print 'Agencia: %s e Conta: %s' % (conta.agencia, conta.numero)
print 'Saldo:', str(conta.saldo)

# Teste dos métodos depositar() e sacar()
conta.depositar(500.0)
try:
    conta.sacar(2500.0)
except ValueError as error:
    print 'Erro: %s' % error
except  SaldoInsuficienteError as error:
    print 'Erro: %s' % error

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
