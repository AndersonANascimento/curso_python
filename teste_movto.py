# -*- coding: UTF-8 -*-
from model import ContaBancaria
from model import Cliente
from model import Movimentacao

contas = [] # Lista de Contas

num_contas = 2 # Numero de contas

for i in range(num_contas):
    print 10 * '-', 'Cadastro de Contas', 10 * '-'
    cliente = Cliente()
    cliente.nome = raw_input('Nome: ')
    cliente.cpf = raw_input('CPF: ')
    cliente.email = raw_input('E-mail: ')

    conta = ContaBancaria()
    conta.cliente = cliente     # vincula cliente a nova conta criada
    conta.agencia = raw_input('Agencia: ')
    conta.numero = raw_input('Número da Conta: ')
    conta.saldo = input('Saldo: ')

    num_movto = input('Deseja informar quantas movimentações? ')
    for j in range(num_movto):
        movto = Movimentacao()
        movto.data = raw_input('Data Movimentação: ')
        movto.descricao = raw_input('Descrição da Movimentação: ')
        movto.valor = input('Valor da Movimentação: ')
        conta.movimento.append(movto)   # add movimentação da conta na lista

    contas.append(conta)    # add conta criada na lista

for i in range(len(contas)):
    print 'Nome:', contas[i].cliente.nome
    print 'CPF:', contas[i].cliente.cpf
    print 'E-mail:', contas[i].cliente.email
    print 'Agencia: %s e Conta: %s' % (contas[i].agencia, contas[i].numero)
    print 'Saldo:', contas[i].saldo
    movto = contas[i].movimento
    for j in range(len(movto)):
        print 'Movimento: %s no valor de %.2f em %s' % (movto[j].descricao, movto[j].valor. movto[j].data)

