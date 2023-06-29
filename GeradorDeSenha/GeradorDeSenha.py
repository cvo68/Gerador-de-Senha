import random

print('Aqui e seu gerador de senhas!!')

char = 'abcdefghijklmnopqrstuvwxyz0123456789'

num = int(input('Quantas senhas voce deseja: '))
tam = int(input('Qual o tamanho das senhas: '))

if num == 0:
    print('Voce nao quer nenhuma senha!!')
else:
    print('Aqui esão as suas senhas: ')

for snh in range(num):
    senha = ''
    for cont in range(tam):
        senha = senha + random.choice(char)
    print(senha)
     

