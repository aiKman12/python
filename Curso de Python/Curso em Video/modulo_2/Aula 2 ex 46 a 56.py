'''
# 46 Faça um que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 
# até 0, com uma pausa de 1 segundo entre eles.
import time

for c in range(10, -1, -1):
        print(c)
        time.sleep(1)
print('Estouro de fogos')

# 47 Crie que mosta todos os numeros pares que estao no intervalo entre 1 e 50.
for c in range(1 , 50, 2):
    print(c + 1, end=' ')

# 48 Que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram 
# no intervalo de 1 ate 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if  c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todo os {} valores solicitados é {}'.format(cont, soma))

# 49 refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando
# um laço for.
print('-'*20)
a = int(input('Informe um numero: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(a, c, (a * c)))
print('-'*20)

# 50 que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado 
# for impar, desconsedere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe o {}º numero: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numeros pares e a soma dos numeros foi {}'.format(cont, soma))

# 51 que leia e primeiro termo e a razao de uma Progração aritimetrica. No final mostre os 10 primeiros
# termos dessa progressao.
primeiro_termo = int(input('Primeiro termo: '))
razao =  int(input('Razão: '))
decimo = primeiro_termo + (10-1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print('{} '.format(c), end='→ ')
print('ACABOU')

# 52 que leia um numero inteiro e diga se ele é ou nao um numero primo.
num = int(input('Informe um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:       
    print('O numero é primo.')
else:
    print('Nao é um numero primo.')

# 53 que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
a = str(input('Escreva uma frase todas minusculas e ve se é um palindromo: ')).replace(' ','')
b = a[::-1]
if a == b:
    print('A Frase "{}" é um palindromo:'.format(b))
else:
    print('A Frase "{}" não é um palindromo.'.format(b))
print('A frase inserida "{}"'.format(a))
# --------------------------------ou-------------------------
frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo')

# 54 crie um que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda nao 
# atingiram a maioridade e quantas ja sao maiores.
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input('Insira o ano de nasicmento da {}ª pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))

# 55 leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))
'''
# 56 que leia nome, idade e sexo de 4 pessoas. No final o programa mostra.
# a media de idade do grupo, qual é o nome do mais velho, quantas mulheres tem menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print("----- {}ª PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
