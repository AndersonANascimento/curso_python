# -*- coding: UTF-8 -*-
from model import Seguranca, Diretor, Gerente
from control import ControladorBonus

ctl = ControladorBonus()

seg = Seguranca(dia_servico='seq, qua, sex', salario=800)
ctl.lista = seg

dir = Diretor(1234, 5000.0)
ctl.lista = dir

ger = Gerente(senha=5678, horario_atendimento='10:00 - 12:00', salario=3500)
ctl.lista = ger


print len(ctl.lista), ctl.total
ctl.excluir(seg)
print len(ctl.lista), ctl.total