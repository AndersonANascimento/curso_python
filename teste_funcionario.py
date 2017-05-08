# -*- coding: UTF-8 -*-
from model import Funcionario

f = []

f1 = Funcionario()
f2 = Funcionario('Anderson', 'anderson.a.nascimento@gmail.com', 12000.0)
f3 = Funcionario(salario=5555.5)

f.append(f1)
f.append(f2)
f.append(f3)

for i in range(len(f)):
    print '\nMatricula:', f[i].matricula
    print 'Nome:', f[i].nome
    print 'Email:', f[i].email
    print 'Salario:', f[i].salario
