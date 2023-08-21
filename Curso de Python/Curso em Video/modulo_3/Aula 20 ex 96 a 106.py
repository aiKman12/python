'''
# 96 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l, c):
    a = l * c
    print(f'A area do terreno de {l}x{c} é {a}m²')

# programa principal
print(' Controle de Terrenos.')
print('-' * 20)

l = float(input('Qual a largura (m)? '))
c = float(input('Qual o comprimento (m)? '))
area(l, c)

# 97 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como 
# parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Ola mundo!') Saida:
#~~~~~~~~~
#Olá, Mundo!
#~~~~~~~~~

def escreva(msg):
    tam = len(msg) + 3  #Vai sair o ~ do tamanho do texto + 4 ~
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)

escreva('Oi')
escreva('Curso de Pyton no Youtube')
escreva('Curso em Video')

# 98 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizadade
from time import sleep

def contador(i, f, p):
    print('=' *30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p            
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.2)
            cont -= p
        print('FIM!')

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' *30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

# 99 Faça um programa que tenha uma função chama maior(), que receba varios valores inteiros. 
# Seu programa tem que analizar todos os valores e dizer qual deles é maior.
# (desempacotamento)
def maior(* valores):
    print(f'Os valores informados foram {valores} e o maior valor é {max(valores)}.')

valores = []

# programa princial
while True:
    val = int(input('Informa um valor. '))
    valores.append(val)
    continuar = str(input('Deseja continurar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

maior(* valores)

# ------------------------------ OU ----------------------
from time import sleep

def maior(* num):
    cont = maior = 0
    print('=' *30)
    print('Analizando os valores passados')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}.')

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# 100 Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 umeros e vai colocaços dentro da lista.
# a segunda funçao via mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

numeros = []

def sorteia():
    for alea in range(5):
        alea = randint(1, 100)
        numeros.append(alea)
        numeros.sort()
        print(f'{alea}', end=' ')
        sleep(0.3)
    print('PRONTO!')
    print(f'Os numeros em ordem crescente são: {numeros}.')

def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos numeros pares é {soma}.')

sorteia()
somaPar()

# 101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(nascimento):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nascimento
    print(f'Você tem {idade} anos de idade. ')
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    elif idade < 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'

nascimento = int(input('Qual o seu ano de nascimento. '))
print(voto(nascimento))

# 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e 
# outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    """
    Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# programa principal
num = int(input('Informe um numero para calcular o fatorial: '))
show = str(input('Quer ver o calculo ? [S/N] ')).upper().strip()[0] == 'S'

print(fatorial(num, show))

# 103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols 
# ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# programa principal
nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

# 104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo 
# a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero valido')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')

# 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:
# Quantidade de notas, Maior nota, Menor nota, media da turma, a sutuação(opcional)
def notas(*n, sit = False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

    #programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
'''
# 106 Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
