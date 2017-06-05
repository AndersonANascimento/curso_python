# -*- encoding=UTF-8 -*-
# Resolução de Exercícios da Apostila 01
# Slide 26
string = '!! ! a;b;c;d;e;f;gh!########'
print string.strip(' !#h').split(';')

string = 'ring ring! - hello!'
print string[string.find('hello'):];
# ou
print string[13:]

string = 'isso deve ser bom'
print string.title()


# Slide 33
# n1 = input('Informe o 1º número: ')
# n2 = input('Informe o 2º número: ')
# if n1 > n2:
#     print n1
# elif n2 > n1:
#     print n2
# else:
#     print 'Números são iguais!'

# letra = raw_input('Informe o sexo ("M/F"): ')
# if letra.upper() == 'M':
#     print 'Masculino'
# elif letra.upper() == 'F':
#     print 'Feminino'
# else:
#     print 'Sexo inválido!'

# Slide 42
# n = input('Informe o número da tabuada: ')
# for i in range(0, 11):
#     print n, ' X ', i, ' = ', n * i

# print sum(range(1, 100, 2))

# while True:
#     frase = raw_input('Digite a frase: ')
#     if frase.upper().__eq__('SAIR'):
#         break
#     print frase

# Slide 48
def fat(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


print fat(5)


def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# for i in range(1, 101):
#     if primo(i):
#         print i, ' é primo.'

# Exemplo Listas
lista = range(1, 6)
print lista
print lista[0]
lista.append(0)
print lista
lista.insert(0, lista[5])
print lista
print lista.count(0)
lista.remove(5)
print lista
removido = lista.pop(5)
print lista, removido
print lista.index(3)

lista.reverse()
print lista
lista.sort()
print lista

# Exemplo Tuplas
tupla = (1, 2, 3)
print tupla

# Exemplo Dicionários
dicionario = {'key': 'value', 2: 4}
print dicionario['key']
print dicionario[2]

dicionario['nome'] = 'Anderson'
print dicionario

dicionario.pop(2)
print dicionario

print dicionario.get('sobrenome', 'Não existe')
print dicionario.has_key('nome')

dicionario.clear()
print dicionario


# Slide 59
def fibo(n):
    fibs = [0, 1]
    for i in range(n - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


print fibo(3)

lista = [1, 4, 15, 26, 3, 6, 10, 13, 5, 3]


def countSupX(lista, x):
    count = 0
    for i in lista:
        if i > x:
            count += 1
    return count


print countSupX(lista, 3)


# notas = {}
# for i in range(3):
#     nome = raw_input('Nome: ').upper()
#     nota = input('Nota: ')
#     notas[nome] = nota
# print notas

def escada(string):
    for i in range(len(string)):
        print string[:i + 1]


print escada('TESTE')
