# -*- coding: UTF-8 -*-
class ContaBancaria(object):
	def __init__(self):
		self.agencia = None
		self.numero = None
		self.cliente = None
		self.saldo = 0.0
		self.movimento = []

	def depositar(self, valor):
		self.saldo += valor

	def sacar(self, valor):
		if self.saldo >= valor:
			self.saldo -= valor
			return True
		return False

	def transferir(self, valor, destino):
		if self.sacar(valor):
			destino.depositar(valor)
			return True
		return False

class Cliente(object):
	def __init__(self):
		self.nome = None
		self.cpf = None
		self.rg = None
		self.email = None

class Movimentacao(object):
	def __init__(self):
		self.data = None
		self.descricao = None
		self.valor = None