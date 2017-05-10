# -*- coding: UTF-8 -*-
class ControladorBonus(object):
    def __init__(self, lista=[]):
        self.__lista_funcionarios = lista
        self.__total = 0.0

    @property
    def total(self):
        return sum(f.bonus for f in self.__lista_funcionarios)

    @property
    def lista(self):
        return self.__lista_funcionarios

    @lista.setter
    def lista(self, item):
        self.__lista_funcionarios.append(item)
        self.__total += item.bonus

    def excluir(self, item):
        self.__total -= item.bonus
        return self.__lista_funcionarios.remove(item)
