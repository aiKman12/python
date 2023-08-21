'''
# 90 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.
dados = {}

for d in range(1):
    dados['nome'] = str(input('Qual o seu nome? '))
    dados['media'] = float(input(f'Qual a sua media de {dados["nome"]}? '))

if dados['media'] < 5:
    media = 'REPROVADO'
elif dados['media'] >= 7:
    media = 'APROVADO'
else:
    media = 'RECUPERAÇÃO'

print('=' * 30)
print(f'O nome é {dados["nome"]}.')
print(f'A media foi {dados["media"]}.')
print(f'A situação é de {media}')

# 91 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
#  sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter     # se for em 0 coloca em ordem de key e 1 para values;

result = {}
ranking = list()

for a in range(4):
    result[a+1]= randint(1, 10)
for k, v in result.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)
print('=' * 30)

ranking = sorted(result.items(), key=itemgetter(1), reverse=True)   # Reverse para ficar ao contrario
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: Jogador {v[0]} com {v[1]}')
    sleep(1)

# 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
#  em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

dados = {}

dados['nome'] = str(input('Qual o teu nome? '))
nasc = int(input('Em que ano nasceu? '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Possue carteira de trabalho (0 se não possui)? "))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Qual o ano de contratação? '))
    dados['salario'] = float(input('Qual o salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('#'*35)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

print('#'*35)

# 93 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome 
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. ,
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = list()

cont = 0

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for g in range(tot):
    partidas.append(int(input(f'    Quantos gols na partida {g}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)    #soma o que esta na lista partidas e cria dentro da lsta o total

print('+='* 25)
print(jogador)
print('+=' * 25)

for k,v in jogador.items():
    print(f'O campo {k} em o valor {v}')

print('+=' * 25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partita {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]}')

# 94 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa 
# em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média
galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('M/F: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo temo {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ',end='')
print()
print(f'Lista das pessoas que estao acima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')
'''
# 95 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um 
# sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
partidas = list()
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)    #soma o que esta na lista partidas e cria dentro da lsta o total
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-' * 40)
print('cod' , end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTEMNTO DE JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')