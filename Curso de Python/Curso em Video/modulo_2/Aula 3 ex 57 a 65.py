'''
# 57 faça um que leia o sexo de uma pessoa, mas so aceite os valores M ou F. Caso esteja errado peça a digitação novamento até um 
# valor correto.
while True:
    c = str(input('Informe o seu sexo [M/H]: ')).upper()
    if c == 'M':
        print('Obrigado Senhora.')
        break
    if c == 'H':
        print('Obrigado Senhor')
        break
    else:
        print('Valor errado.')

# 58 Melhore o jogo desafio 28 onde o computador vai pensar em um numero entre 0 e 10. So que agora o joador vai 
# tentar adivinhar até acertar mostrando no final quantos palpites fora necessarios para vencer
from random import randint
cont = 0
comp = randint(0, 10)

while True:
    pessoa = int(input('Escolha um numero entre 0 e 10: '))
    cont += 1
    if comp == pessoa:
        print('Acertou em {} palpites.'.format(cont))
        break
    else:
        print('Tente novamente.')

# 59 crei que leia dois valores e mostre um menu na tela: 1 somar, 2 multiplicar, 3 maior, 4 novos numeros, 
# 5 sair do programa. Seu programa devera realizar as operaçao solicitada em cada caso. 
valor1 = float(input('Informe o primeiro valor: '))
valor2 = float(input('Informe o segundo valor: '))

while True:
    print('-'*30)
    print(#Qual operaçao deseja executar?
[ 1 ] SOMAR.
[ 2 ] MULTIPLICAR.
[ 3 ] MAIOR.
[ 4 ] NOVOS NÚMEROS.
[ 5 ] SAIR DO PROGRAMA.)
    print('-'*30)
    opçao = int(input('Informe o numero da operação escolhida: '))
    if opçao == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
    elif opçao == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif opçao == 3:
        if valor1 < valor2:
            print('O 1º valor {} é menor que o 2º valor {}'. format(valor1, valor2))
        elif valor1 > valor2:
            print('O {} é maior que {}'.format(valor1, valor2))
        else:
            print('O {} e {} são iguais.'.format(valor1, valor2))
    elif opçao == 4:
        valor1 = float(input('Insira o primeiro novo valor: '))
        valor2 = float(input('Insira o segundo novo valor: '))
    elif opçao == 5:
        break
    else:

# 60 Faça um que leia um numero qualquer e mostre o seu fatorial. ex: 5!=5x4x3x2x1=120
num = int(input('Informe um numero para saber seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '= ', end ='')
    f *= c
    c -= 1
print('{}'.format(f))
    

# 61 Refaça o desafio 51 lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao 
# usando a estrutura while

primeiro_termo = int(input('Primeiro termo: '))
razao =  int(input('Razão: '))
termo = primeiro_termo
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')

# 62 melhor o desafio 61 peguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando 
# ele disser que quer usar 0 termos.
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")

# 63 escreva um que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci. 
# Ex: 0-1-1-2-3-5-8
num = int(input('Quantos termos quer mostrar: '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end=' ')
cont = 3

while cont <= num:
    t3 = t1 + t2
    print('{}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')    
'''
# 64 crie um que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles 
# (desconsiderando o flag)
cont = soma = num = 0
while num != 999:
    num = int(input('Insira um numero qualquer [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print('Voce digitou {} numeros e a soma entre eles sao de {}.'.format(cont, soma))
'''
# 65 crie um que leia varios numeros inteiros pelo teclado. No final da execução mostre a media entre todos os valores
# e qual foi o maior e o menor valor lido. O programa deve perguntar ai usuario se ele quer ou nao continuar a digitar 
# os valores.
soma = quant = maior = menor = 0
continuar = 'S'

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
'''
