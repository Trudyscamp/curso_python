# Exercício
# Peça ao usuário para digitar seu nome
name = input('Enter your name: ')
# Peça ao usuário para digitar sua idade
age = input('Enter your age: ')
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome} x
#         Seu nome invertido é {nome invertido} x
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras x
#         A primeira letra do seu nome é {letra} 
#         A última letra do seu nome é {letra}

if name != None:
  print(f'Your name is: {name}')
  print('Your name inverted is: ' + name[::-1])
  print('Your name have : ' , len(name) , 'letters')
  print('Your first name letter is: ' )
# Se nada for digitado em nome ou idade: 
#     exiba "Desculpe, você deixou campos vazios."