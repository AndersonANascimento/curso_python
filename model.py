# -*- coding: UTF-8 -*-
class ContaBancaria(object):
    __contador = 0
    def __init__(self, saldo=0.0):
        self.agencia = None
        self.numero = None
        self.cliente = None
        self.__saldo = saldo
        self.movimento = []
        # incrementa o contador
        ContaBancaria.__contador += 1

    @staticmethod
    def contador():
        return ContaBancaria.__contador

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
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

class Funcionario(object):
    __contador = 0

    def __init__(self, nome=None, email=None, salario=950.0):
        # incrementa o contador
        Funcionario.__contador += 1
        # matricula auto-incremento
        self.__matricula = Funcionario.__contador
        self.nome = nome
        self.email = email
        self.salario = salario

    @property
    def matricula(self):
        return self.__matricula

class Seguranca(Funcionario):
    def __init__(self, dia_servico=None, salario=None):
        # Inicializa os atributos da classe Pai
        Funcionario.__init__(self, salario=salario)
        self.dia_servico = dia_servico

class Diretor(Funcionario):
    def __init__(self, senha=None, salario=None):
        Funcionario.__init__(self, salario=salario)
        self.senha = senha

    def efetuar_login(self, senha):
        return self.senha == senha

class Gerente(Funcionario):
    def __init__(self, senha=None, horario_atendimento=None, salario=None):
        Funcionario.__init__(self, salario=salario)
        self.senha = senha
        self.horario_atendimento = horario_atendimento

    def efetuar_login(self, senha):
        return self.senha == senha