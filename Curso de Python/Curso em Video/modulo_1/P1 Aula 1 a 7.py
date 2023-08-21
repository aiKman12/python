'''
# Desafio 1
nome = input ('Qual é o seu nome? ')
print('Ola', nome, '! Prazer em te conhecer!')

# Desafio 2
dia = input ('Dia = ')
mes = input ('Mês = ')
ano = input ('Ano = ')
print('Você nasceu dia', dia, 'de', mes, 'de', ano, '. Correto?')

# Desafio 3
n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número '))
soma = n1+n2
print('A soma é ', soma)

# Exercicio 1
nome = input ('Qual o seu nome? ')
idade = input ('Qual sua idade? ')
peso = input ('Qual o seu peso? ')
print(nome, idade, peso)

# Exercicio 2
nome = input(' Digite seu nome ')
print('É um prazer em te conhecer, {}!'.format(nome))

n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número '))
soma = n1+n2
print('A soma entre {} e {} vale {}'.format(n1,n2,soma))

n = input('Digite algo ')
print(n.isnumeric())

# Desafio 4
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numro: '))
soma=n1+n2
print('A soma entre {} e {} é {}'.format(n1,n2,soma))

a=input('Escreva o que quiser: ')
print('O tipo primitivo desse valor é ',type(a))
print('É um alfabetico? ', a.isalpha())
print('É um numerico? ', a.isalnum())
print('É um alfa numero em ingles?', a.isascii())
print(a.isdigit())
print('É um numero decimal? ', a.isdecimal())

print('='*20)  # imprimi 20x o =
print('5'*20)  # imprimi 20x o numero 5

nome = input('Qual é o seu nome')
print('Prazer em conhecer {:20}!'.format(nome))  # Escreve o nome em um espaço de 20 caracteres
print('Prazer em conhecer {:>20}!'.format(nome)) # Escreve a direita em 20 espaços
print('Prazer em conhecer {:<20}!'.format(nome)) # Escreve a esquerda dos 20 espaços
print('Prazer em conhecer {:^20}!'.format(nome)) # Centralizado dentro dos 20 espaços
print('Prazer em conhecer {:=^20}!'.format(nome)) # Centraliza entre 20 e coloca = entre os espaços

n1 = int(input('Digita um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, \n o produto é {} e a divisao é {:.3f} '.format(s,m,d), end='') # :.3f significa depois da , 3 casas decimais e f de float
print('A divisao inteira {} e potencia {}'.format(di,e))               # o end='' (significa que nao vai ter quebra de linha)
'''