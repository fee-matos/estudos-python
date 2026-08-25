nome = 'Fernando Matos'
altura = 1.75
peso = 67
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura',)
print('pesa', peso, 'quilos e seu IMC é', imc,)

# Fernando Matos tem 1.75 de altura,
# pesa 67 quilos e seu IMC é
# 21.877551020408163

# outros jeitos de fazer a conta.
conta_imc = 67 / (1.75 * 1.75)
print(conta_imc)

conta_imc2 = peso / altura ** 2
print(conta_imc2)