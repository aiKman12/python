'''
t = int(input('Quando anos tem seu carro? '))
if t <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

t = int(input('Quando anos tem seu carro? '))
print('Carro novo' if t<=3 else 'Carro Velho')
print('--FIM--')

a = str(input('Qual é o seu nome: '))
if a == 'Gustavo':
    print('Que nome lindo voce tem!')
print('Bom dia {}'.format(a))

a = str(input('Qua o seu nome? '))
if a == 'Iuri':
    print('Que nome lindo nome voce tem!')
else:
    print('Seu nome é comum né!')
print('Bom dia {}'.format(a)) '''

print('\033[4;30;45m Olá mundo!\033[m') # mudar as cores de fundo