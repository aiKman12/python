'''
# 78 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = []

for n in range(0, 5):
    lista.append(int(input('Digita um numero: ')))
print(lista)
print('-'*30)
for num, v in enumerate(lista):
    print(f'O valor [{v}] esta na posição [{num}] na lista.')

print(f'O maior valor foi o [{max(lista)}].')
print(f' O menor valor foi o [{min(lista)}]')

# 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os 
# valores únicos digitados, em ordem crescente.
lista = list()

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        continuar = str(input('Voce deseja continuar [S/N]? ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Resposta inválida! Tente novamente.')
    if continuar == 'N':
        break

lista.sort()
print(f'Os numeros digitados foram: {lista}')

# 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []

for n in range(0, 5):
    num = int(input('Insira um numero: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')

# 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []

while True:
    lista.append(int(input('Informe um numero: ')))
    continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while continua not in 'SN':
        print('Valor incorreto.')
        continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break

print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'Os numero digitados em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')

# 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas 
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []

while True:
    v = int(input('Informe um valor: '))
    lista.append(v)
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while continua not in 'SN':
        print('Resposta inválida! Tente novamente.')
        continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
    
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')

# 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados 
# na ordem correta.
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# 84 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
mais_pesadas = []
mais_leves = []
maior = menor = 0

while True:
    nome = str(input('Qual o seu nome? '))
    peso = float(input('Qual o seu peso? '))
    lista.append([nome, peso])

    if len(lista) == 1 or peso > maior:
        maior = peso
        mais_pesadas = [[nome, peso]]
    elif peso == maior:
        mais_pesadas.append([nome, peso])

    if len(lista) == 1 or peso < menor:
        menor = peso
        mais_leves = [[nome, peso]]
    elif peso == menor:
        mais_leves.append([nome, peso])

    continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while continua not in 'SN':
        print('Resposta inválida! Tente novamente.')
        continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break

print(f'Foram cadastrados {len(lista)} pessoas.')
print('As mais pesadas são: ')
for p in mais_pesadas:
    print(f'{p[0]} com {p[1]}Kg')
print('As mais leves são: ')
for p in mais_leves:
    print(f'{p[0]} com {p[1]}Kg')

# 85 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = []
par = []
impar = []

for v in range(0, 7):
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()

print(f'Foram digitados {len(lista)} numeros e eles sao: {lista}')
print(f'Os numeros pares sao: {par}')
print(f'Os numeros impares sao: {impar}')

# ------------------------ ou -----------------------------
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

# 86 Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, 
# mostre a matriz na tela, com a formatação correta.
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para [{i},{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('Matriz 3x3:')
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end='')
    print()

# ------------------  ou --------------------------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):           # esse range alimenta as linhas
    for c in range(0, 3):       # esse alimenta as colunas
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-=' *30)

for l in range(0, 3):       # esse range é apenas para mostrar a formatação por isso é igual
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')   # o ^5 cinco casas vazias e centralizado
    print()         # esse print quebra a linha

# 87 Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# soma dos valores da terceira coluna.
# O maior valor da segunda linha.
matriz = []
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para [{i},{j}]: '))
        linha.append(valor)
        
        if valor % 2 == 0:
            soma_pares += valor
            
        if j == 2:
            soma_terceira_coluna += valor
            
        if i == 1 and valor > maior_segunda_linha:
            maior_segunda_linha = valor
            
    matriz.append(linha)

print('Matriz 3x3:')
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end='')
    print()

print(f'A soma de todos os numeros pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')

# ------------------------------  ou  -----------------------------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):           # esse range alimenta as linhas
    for c in range(0, 3):       # esse alimenta as colunas
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

print('-=' *30)

for l in range(0, 3):       # esse range é apenas para mostrar a formatação por isso é igual
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')   # o ^5 cinco casas vazias e centralizado
        if matriz[l][c] % 2 == 0:
            spar = matriz[l][c]


    print()         # esse print quebra a linha
print('-=' *30)
print(f'A soma de todos os numeros pares é: {spar}')
print(f'A soma dos valores da terceira coluna é: {scol}')
print(f'O maior valor da segunda linha é: {mai}')

# 88 Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
lista = []

qtd = int(input('Quantos jogos deseja? '))

for c in range(qtd):
    jogo = []
    while len(jogo) < 6:
        auto = randint(1, 60)
        if auto not in jogo:
            jogo.append(auto)
    jogo.sort()
    lista.append(jogo)
for i, jogo in enumerate(lista):
    print(f'Jogo {i+1}: {jogo}')
'''
# 89 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
# individualmente.
alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    continua = input('Deseja continuar? [S/N] ')
    if continua in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')    # :<4 impsso imprime a string "No." alinhada à esquerda em um campo de 4 caracteres de largura. O sinal de menor < é usado para alinhamento à esquerda.
print('-' * 26)

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
