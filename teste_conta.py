from model import ContaBancaria
#  ou
# import model.ContaBancaria # Não é boa prática

conta = ContaBancaria() # Cria nova instância
conta.agencia = '3715'
conta.numero = '2171-7'
conta.nome_cliente = 'Anderson'
conta.saldo = 1500.0

print 'Agencia:', conta.agencia, 'Conta:',conta.numero
print 'Cliente:', conta.nome_cliente, 'Saldo:', conta.saldo
