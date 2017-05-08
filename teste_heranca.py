# -*- coding: UTF-8 -*-
from model import Funcionario
from model import Seguranca
from model import Diretor
from model import Gerente

funcionario = Funcionario(salario=1000)
seguranca = Seguranca(dia_servico='seq, qua, sex', salario=800)
diretor = Diretor(1234, 5000.0)
gerente = Gerente(5678, '10:00 - 12:00', 3500)

print 'Funcionário\nMatrícula:', funcionario.matricula
print 'Salário:', funcionario.salario

print '\nSegurança\nMatrícula:', seguranca.matricula
print 'Salário:', seguranca.salario
print 'Dias de serviço:', seguranca.dia_servico

print '\nDiretor\nMatrícula:', diretor.matricula
print 'Salário:', diretor.salario
print 'Senha:', diretor.senha

if diretor.efetuar_login(1111):
    print 'Diretor logado'
else:
    print 'Falha na autenticação do Diretor'

print '\nGerente\nMatrícula:', gerente.matricula
print 'Salário:', gerente.salario
print 'Senha:', gerente.senha
print 'Atendimento:', gerente.horario_atendimento

if gerente.efetuar_login(5678):
    print 'Gerente logado'
else:
    print 'Falha na autenticação do Gerente'