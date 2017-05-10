# -*- coding: UTF-8 -*-
from model import Seguranca, Diretor, Gerente
from control import ControladorBonus

ctl = ControladorBonus()

seg = Seguranca(dia_servico='seq, qua, sex', salario=800)
ctl.lista = seg

ger = Gerente(5678, '10:00 - 12:00', 3500)
ctl.lista = ger

dir = Diretor(1234, 5000.0)
ctl.lista = dir

print len(ctl.lista), ctl.total
ctl.excluir(seg)
print len(ctl.lista), ctl.total