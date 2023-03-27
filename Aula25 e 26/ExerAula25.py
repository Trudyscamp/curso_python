#Criar 3 produtos.
prod1 = 'Processor'
prod2 = 'Motherboard'
prod3 = 'Memory'
#Definir seus precos.
price1 = 120
price2 = 200
price3 = 80
#Definir o numero hexadecimal do produto.
hex1 = 22
hex2 = 26
hex3 = 30
#definir o produto.
res1 = '%s, has a price of U$%.2f' % (prod1, price1) + '\n'
res2 = '%s, has a price of U$%.2f' % (prod2, price2) + '\n'
res3 = '%s, has a price of U$%.2f' % (prod3, price3) + '\n'
#imprimir o produto e o codigo de produto.
print(res1,res2,res3)
print('Hex of %s is: %08X' % (prod1, hex1))
print('Hex of %s is: %08X' % (prod2, hex2))
print('Hex of %s is: %08X' % (prod3, hex3))
