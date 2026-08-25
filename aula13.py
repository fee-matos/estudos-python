nome = 'Fernando Matos'
altura = 1.75
peso = 67
imc = peso / (altura * altura)

"f-strings"
Linha_1 = f'{nome} tem {altura:,.2f} de altura'
Linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(Linha_1)
print(Linha_2)

# Fernando Matos tem 1.75 de altura,
# pesa 67 quilos e seu IMC é
# 21.877551020408163