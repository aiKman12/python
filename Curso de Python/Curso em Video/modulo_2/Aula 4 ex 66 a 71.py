'''
# 66 crie um que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999, 
# que é a condição de parada. No final mostre quantos foram digitados e qual foi a soma entre
soma = cont = 0

while True:
    num = int(input('Informe um numero ou [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Voce digitou {cont}x e a soma deles são {soma}.')

# 67 que mostre a tabuada de varios numeros, um de cada vez, para o valor digitado pelo usuario. 
# O programa sera interrompido quando o numero soficitado foi negativo

while True:
    n = int(input('Voce quer saber a tabuada de qual numero? '))
    if n > 0:
        print('-' * 10)
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
        print('-' * 10)
    else:
        break
print('FIM')

# 68 que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogar perder, 
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
from random import randint
vitorias = 0

while True:
    usuario = int(input('Escolhe um numero: '))
    escolha = str(input('Escolha PAR(P) ou IMPAR(I): ')).upper().strip()[0]
    pc = randint(0, 100)
    total = usuario + pc
    resultado = 'par' if total % 2 == 0 else 'impar'
    
    if escolha == resultado[0]:
        print(f'Voce jogou {usuario} e o computador {pc}. \nTotal de {total} deu {resultado.upper()}')
        print('Você VENCEU!\nVamos jogar novamente...')
        vitorias += 1
    else:
        print(f'Você jogou {usuario} e o computador {pc}. Total de {total} deu {resultado.upper()}')
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')

# 69 crie um que leia a idade, o sexo de varias pessoas. A cada pesso cadastrada o programa devera 
# perguntar se o usuario quer ou nao constinuar. no final mostre: 
# A) quantas pessoas tem mais de 18 anos. 
# B) quantos homens foram cadastrados. 
# C) quantas mulheres tem menos de 20 anos
maior_18 = 0
qtd_homens = 0
mmenor_20 = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
        
    if idade >= 18:
        if idade >= 18:
            maior_18 += 1
        if idade <= 20 and sexo =='F':
            mmenor_20 += 1
        if sexo == 'M':
            qtd_homens += 1
    continua = str(input('Quer continuar [S/N]: ')).upper().strip()
    if continua == 'N':
        break
print(f'{maior_18} pessoas tem mais de 18 anos. \n{qtd_homens} homens foram cadastrados. \n{mmenor_20} mulheres tem menos de 20 anos.')

# 70 um que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai
# continuar. no final mostre. 
# A) qual o total gasto na compra. 
# B) quantos produtos custam mais de 1000. 
# C) qual é o nome do mais barato
total = maior1000 = contador = 0
mais_barato = ''
preço_mais_barato = float('Inf')

while True:
    nome_produto = str(input('Qual o nome do produto: ')).lower().strip()
    preço_produto = float(input('Qual o preço do produto: '))
    contador += 1
    total += preço_produto

    if preço_produto > 1000:
        maior1000 += 1
    if preço_produto < preço_mais_barato:
        preço_mais_barato = preço_produto
        mais_barato = nome_produto
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Voce deseja continuar [S/N]? ')).lower().strip()
    if continua ==  'n':
        break

print(f'O total gasto na compra foi de R${total:.2f}.')
print(f'{maior1000} produtos custam mais que R$1.000,00.')
print(f'O produto mais barato foi {mais_barato} que custa R${preço_mais_barato:.2f}.')
'''
# 71 simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a
# ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS: considere que o caixa possui cedulas de 50, 20, 10 e 1.
valor = int(input('Qual valor você quer sacar? R$'))

total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
