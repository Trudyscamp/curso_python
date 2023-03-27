#nome
#peso
#resultado
#IMC = PESO / (ALTURA*ALTURA)

nome = 'Eduardo Vynnicius'
altura = 1.73
peso = 70
imc = peso / (altura*altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'{nome} pesa {peso} e seu imc é: '
linha_3 = f'{imc:.2f}'
print('Seu nome é: ' + nome)
print(linha_1)
print(linha_2)
print(linha_3)
