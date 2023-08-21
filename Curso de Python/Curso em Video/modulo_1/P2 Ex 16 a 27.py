'''
# 16 Que leie um numero real qualquer pelo teclado e mostre na tela
# a sua porção inteira
# ex: 6.127. O numero 6,127 tem a parte inteira 6
import math
n = float(input('Isira um numero qualquer. '))
print('O número {} possui a sua parte inteira de {}'.format(n, math.ceil(n)))

# 17 que leie o comprimento do cateto oposto e cateto adjancente 
# de um triangulo, calcule e motre o comprimento da hipotenusa.
import math
a = float(input('Informe o primeiro cateto: '))
b = float(input('Informe o segundo cateto: '))
h = math.hypot(a, b)
print('A hipotenusa de {} e {} é {:.2f}'.format(a, b, h))

# 18 que leie um angulo qualquer e mostre na tela o valor de seno,
# cosseno e tangente desse angulo
from math import radians, sin, cos, tan
n = float(input('Informe um número: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('O numero {:.2f} possui: \nSeno {:.2f} \nCosseno {:.2f} \nTangente {:.2f}'.format(n, s, c, t))

# 19 um professor quer sortear um dos quatro alunos para apagar 
# o quadro. faça que ajude ele, lendo o nome deles e escrevendo 
# o nome escolhido
from random import choice
a = str(input('Informe o primeiro nome: '))
b = str(input('Informe o segundo nome: '))
c = str(input('Informe o terceiro nome: '))
d = str(input('Informe o quarto nome: '))
alu = [a, b, c, d]
sor = choice(alu) #escolha os nomes
print('O aluno escolhido para apagar o quadr é: {}'.format(sor))

# 20 O mesmo professor anterior quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça que leia o nome dos quatro alunos e 
# mostre a ordens sorteadas
from random import shuffle
a = input('Informe o primeiro nome: ')
b = input('Informe o segundo nome: ')
c = input('Informe o terceiro nome: ')
d = input('Informe o quarto nome: ')
alu = [a, b, c, d]
shuffle(alu) #embaralha os nomes
print('Os Alunos sorteados são: ')
print(alu)

# 21 Faça um programa que abra e reproduza o audio de arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('ee.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# 22 Crie que leia o nome completo de um pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem espaços)
# Quantas letras tem o primeiro nome
a = str(input('Informe seu nome completo: '))
print('O seu nome maiusculo é {}'.format(a.upper()))
print('O seu nome minusculo é {}'.format(a.lower()))
print('A quantida de letras em seu nome é de {}'.format(len(a.replace(' ', ''))))
#print('O seu primeiro nome tem {}'.format(a.find(' ')))  #ou a opção de baixo
b = a.split()
print('O Seu primeiro nome é {} e possui {}'.format(b[0], len(b[0])))

# 23 Que leia um numero de 0 a 9999 e mostre na tela cada um dos 
# digitos separados. ex: digite um numero: 4455 (unidade:4, dezena: 3,
# centra 8, milhar:1 )
#a = int(input('Insira um numero entre 0 a 9999: '))
#b = str(a)
#print('Analisando o numero {}'.format(a))
#print('Unidade: {}'.format(b[3]))
#print('Dezena: {}'.format(b[2]))
#print('Centena: {}'.format(b[1]))
#print('Milhar: {}'.format(b[0]))
# ----------ou----------
a = int(input('Insira um numero entre 0 a 9999: '))
b = a // 1 % 10
c = a // 10 % 10
d = a // 100 % 10
e = a // 1000 % 10
print('Analisando o numero {}'.format(a))
print('Unidade: {}'.format(b))
print('Dezena: {}'.format(c))
print('Centena: {}'.format(d))
print(f'Milhar: {e}')

# 24 leia o nome de uma cidade e diga se ela começa ou nao com o nome 'Santo'
a = str(input('Insira o nome de uma cidade: '))
b = a.split()[0]
print('Santo' in b)
print(b.find('Santo'))

# 25 que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
a = str(input('Insira seu nome completo: ')).lower()
print('silva' in a)

# 26 leia uma frase pelo teclado e mostra. Quantas vezes aparace a letra A, 
# em que posição ela aparece a primeira vez, em que posição ela aparece a ultima vez.
a = input('Escreva uma frase: ').lower()
b = a.count('a')
c = a.find('a')
d = a.rfind('a')
print(f'A letra "a" aparece {b} vezes. \nA primeira vez na posição {c}. \nNa ultima posição na {d}')

# 27 que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo 
# nome separadamente. ex: Ana Maria de Souza (primeiro Ana, ultimo Souza),
a = str(input('Informe um nome completo: '))
b = a.split()[0]
c = a.rsplit()[-1]
print('O primeiro nome é {} e o ultimo é {}'.format(b,c))
'''