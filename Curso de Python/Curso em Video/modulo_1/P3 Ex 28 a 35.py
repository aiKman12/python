'''
# 28 Que faça o computador pensar em um numero aleatorio inteiro entre 0 e 5 e peça para o usuario descobrir qual foi o numero 
# escolhido pelo computador. O programa devera escrever na tela se o usuario acertou ou se errou.
import random
a = random.randint(0,5) # faz o computador escolher o numero entre 0 e 5
b = int(input('Tenta advinhar o numero de 0 a 5: '))
print('-=-' * 5)
if a == b:
    print('Acertou')
else:
    print('Errou')
print('Eu pensei em {}'.format(a))
print('-=-' * 5)

# 29 Que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre msg que ele foi multado. A multa custa 7 reias por 
# cada km acima do limite
a = float(input('Informe a velocidade do carro: '))
if a <= 80:
    print('Você passou a {}km/h'.format(a))
    print('Esta dentro do permitido.')
else:
    print('Você foi multado em R${}'.format((a -80 ) * 7))
    print('A multa é de R$ 7,00 por km excedente.')

# 30 que leia um numero inteiro qualquer e mostre na tela se ele é par ou impar.
a = int(input('Infome um numero inteiro: '))
if a % 2 == 0:
    print('O numero {} é Par'.format(a))
else:
    print('O numero {} é Impar'.format(a))

# 31 Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 centavos
# por km para a viagem ate 200km e 0,45 para viagens longas
a = float(input('Informe a distancia de uma viagem em km: '))
if a <= 200:
    print('A passagem custa R$ {:.2f}'.format(a * 0.5))
else:
    print('A passagem custa R$ {:.2f}'.format(a * 0.45))

# 32 Faça que leia um ano qualquer e mostre se ele é bissexto
a = int(input('Informe um ano (ex: 1985): '))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('O ano {} é Bissexto'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))

# 33 Faça um programa que leia 3 numeros e mostre qual é maior e qual é o menor
a = int(input('Informe o primeiro numero '))
b = int(input('Informe o segundo numero '))
c = int(input('Informe o terceiro numero '))
maior = max(a, b, c)
menor = min(a, b, c)
print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior)) 
# -----------------ou --------------------
a = int(input('Informe o primeiro numero '))
b = int(input('Informe o segundo numero '))
c = int(input('Informe o terceiro numero '))
maior = a
menor = a
if b < menor:
    menor = b
else:
    if b > maior:
        maior = b
if c < menor:
    menor = c
else:
    if c > maior:
        maior = c
print('O menor numero é: {}'.format(menor))
print('O maior numero é: {}'.format(maior))

# 34 Um que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a 1250 calcule
# um aumento de 10 % e para inferiores, aumento de 15%
a = float(input('Informe seu salario em R$: '))
if a >= 1250:
    print('Você teve um reajuste de 10% no seu salario de R$ {}, ficando R$ {:.2f}'.format(a, (a * 0.1)+a))
else:
    print('Você teve um reajuste de 15% no seu salario de R$ {}, ficando R$ {:.2f}'.format(a, (a * 0.15)+a))

# 35 Desenvolva que leia o comprimento de 3 seguimentos de retas e diga ao usuario se eles podem ou nao formar um triangulo
a = float(input('Informe o comprimento do primeiro segmento: '))
b = float(input('Informe o comprimento do segundo segmento: '))
c = float(input('Informe o comprimento do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo.')
'''

