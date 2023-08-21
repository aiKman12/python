'''
from math import sqrt, ceil

n = int(input('Digite um Numero '))
m = int(input('Digite outro Numero '))
raiz = sqrt(n)
raiz1 = sqrt(m)
print('A raiz de {} é igual a {:.3f}'.format(n, raiz))
print('A raiz de {} é igual a {}'.format(m, ceil(raiz1)))

import random  # gera numero aleatorio
n = random.randint(1, 10) 
print(n)

frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:3]) 
print(frase[13:])
print(frase[1:13:2])
print(frase[1::2])
print(frase[::2])
print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), 
transformações com replace(), upper(), lower(), capitalize(),
title(), strip(), junção com join().""")

frase = '   Curso em Video Python'
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Video'))
print(frase.lower().find('video'))
div = frase.split()
print(div)
print(div[3])
print(div[3] [3])
'''
