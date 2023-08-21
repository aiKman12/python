'''
# 72 Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extensao, de zero ate 20.
# seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostralo por extenso.
extenso = ('zero', 'um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Insira um numero de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {extenso[n]}')

# 73 Crie uma tupla preenchida com 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação. 
# Depois mostre. Apenas os 5 primeiros colocados. Os ultimos 4 colocados da tabela. Uma lista com os times em ordem 
# alfabetica. Em que posição na tabela esta o time da cuiaba.
times = ("Botafogo", "Flamengo", "Palmeiras", "Grêmio", "Fluminense", "Bragantino", "Athletico-PR", "São Paulo", "Cuiabá", "Cruzeiro", "Fortaleza", "Internacional", "Atlético-MG", "Corinthians", "Santos", "Goiás", "Bahia", "Coritiba", "América-MG", "Vasco")
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print(f'Os times organizados em ordem alfabetica fica: {sorted(times)}')
cuia = times.index('Cuiabá') + 1
print(f'Cuiabá esta na posição {cuia} na tabela.')

# 74 Crie um que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso mostre a listagem de 
# numeros gerados e tambem indique o menos e o maior valor que estao na tupla.
from random import randint

numeros = tuple(randint(1, 100) for _ in range(5))

print(f'Os números gerados foram: {numeros}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')

# 75 Que leia 4 valores pelo teclado e guarde-os em uma tupla. no final. mostre: Quantas vezes apareceu o valor 9. 
# em que posição foi digitado o primeiro valor 3. quais foram os numeros pares.
num = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(4))
# Mostra quantas vezes apareceu o valor 9
print(f'O número 9 apareceu {num.count(9)} vezes.')
# Mostra em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posição {num.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
# Mostra quais foram os números pares
pares = [n for n in num if n % 2 == 0]
print(f'Os números pares digitados foram: {pares}')

# 76 Crie um que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia. No final 
# mostre uma listagem de preços, organizando os dados em forma tabular.
frutas = (
    ("Maçã", 0.5),
    ("Banana", 0.25),
    ("Cereja", 0.75),
    ("Laranja", 0.3),
    ("Manga", 1.0),
    ("Abacaxi", 1.5)
)
for fruta, valor in frutas:
    print(f'{fruta}: {"." * (40 - len(fruta))} R$ {valor:.2f}')
'''
# 77 Crie um programa que tenha um tupla com varias palavra (nao usar acentos). depois disso voce deve mostrar 
# para cada palavra, quais sao suas vogais.
palavras = ("casa", "carro", "bicicleta", "cidade", "livro", "computador", "python", "programacao")

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
