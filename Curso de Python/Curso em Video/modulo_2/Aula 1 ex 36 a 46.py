''''
# 36 Escreva um para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o 
# valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação 
# mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
valor_casa = float(input("Qual o valor da casa? "))
salario = float(input('Qual o seu salario? '))
nvezes = int(input('Em quanta vezes deseja pagar? '))
vmensal = valor_casa / nvezes
limite = salario*0.3
print('-=' * 25)
if vmensal <= limite:
    print('O financiamento foi aprovado em {}x no valor de R${:.2f} '.format(nvezes, vmensal))
else:
    print('O valor passou do limite de 30% do seu salario. \nO credito nao foi aprovado')
print('O valor maximo de parcelas é de R${}'.format(limite))
print('O valor da parcela ficou em R$ {}'.format(vmensal))
print('-=' * 25)

# 37 Escreva que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de 
# conversao, binario, octal, hexadecimal.
a = int(input('Infoma um numero para conversão: '))
print('-=' * 11)
print('Para Binario (1). \nPara Octal (2). \nPara Hexadecimal (3).')
print('-=' * 11)
b = str(input('Escolha um do numero abaixo para a conversão: '))
if b == "1":
    print('O numero {} em decimal é {}'.format(a, bin(a)[2:]))
elif b == "2":
    print('O numero {} em octal é {}'.format(a, oct(a)[2:]))
elif b == 3:
    print('O numero {} em hexadecimal é {}'.format(a, hex(a)[2:]))
else:
    print('Opção Invalida')

# 38 um programa que leia 2 numeros inteiros e compare-os, mostrando na tela. O primeiro valor é maior,
# o segundo é maior, nao existe os dois sao iguais
a = int(input('Iforma um numero: '))
b = int(input('Informa outro numero: '))
if a > b:
    print('O primeiro valor {} é maior que o segundo {}'.format(a, b))
elif a < b:
    print('O segundo valor {} é maior que o primeiro {}'.format(b, a))
else:
    print('Os dois numeros são iguais {}'.format(a))

# 39 Faça que leie o ano de nascimento de um jovem e informe de acordo com a sua idade. Se ele ainda vai
# se alistar ao serviço militar, se é a hora de se alistar ou se ja passou o tempo de alistamento. 
# Seu programa tambem devera mosrtra o tempo que falto ou que passou do prazo.
from datetime import date
a = int(input('Informe o seu ano de nascimento: '))
b = date.today().year - a
print('Você possui {} anos de idade.'.format(b))
if b == 18:
    print('Voce se alistará esse ano de 2023.')
elif b < 18:
    print('Você se alistará em {} ano(s).'.format(18 - b))
else:
    print('Ja passou do tempo de se alistar esta atrasado em {} ano(s).'.format(b - 18))

# 40 crie um que leia 2 notas de aluno e calcule sua media. mostrando no final a mensagem de acordo com 
# a media atingida. Media abaixo de 5 reprovado, media entre 5 e 6.9 recuperação e acima de 7 aprovado
a = float(input('Informe a primeira nota: '))
b = float(input('Informe a segunda nota: '))
m = (a + b) / 2
if m < 5:
    print('REPROVADO')
elif m <= 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

# 41 A confederaçao nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostra sua categoria, de acordo com a idade. Ate 9 anos: mirim, ate 14 infantil, ate 19 junior, 
# ate 20 senior, acima de 20 master.
a = int(input('Informe sua data de nascimento: '))
i = 2023 - a
if i <= 9:
    print('Voce é um jogador Mirim.')
elif i <= 14:
    print('Voce é um jogador Infantil.')
elif i <= 19:
    print('Voce é um jogador Junior.')
elif i <= 20:
    print('Voce é um jogador Senior.')
else:
    print('Voce é um jogar Master.')

# 42 Refaça o desafio 35 e determina se o triangulo é equilatero todos os lados iguais, isoceles dois 
# lados iguais e escaleno todos diferente.
a = float(input('Informe o comprimento do primeiro segmento: '))
b = float(input('Informe o comprimento do segundo segmento: '))
c = float(input('Informe o comprimento do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo.')
    if a == b ==c:
        print('O triangulo equilatero.')
    elif a != b != c != a:
        print('O triangulo é escaleno.')
    else:
        print('O triangulo é isoceles.')
else:
    print('Os segmentos não podem formar um triângulo.')

# 43 que leia o peso e altura de uma pessoa, calcule o imc e mostra o seu status de acordo com a 
# tabela abaixo. abaixo de 18.5 abaixo do peso, entre 18.5 e 25, peso ideal, de 25 a 30 sobrepeso, 
# de 30 a 40 obesidade, acima de 40 obesidade morbida.
a = float(input('Informe seu peso em kg: '))
b = float(input('Informe sua altura em m: '))
imc = a / (b * b)
if imc < 18.5:
    print('Está abaixo do peso.')
elif imc < 25:
    print('Voce esta no peso ideal.')
elif imc < 30:
    print('Voce esta com sobrepeso.')
elif imc < 40:
    print('Voce esta com obesidade.')
else:
    print('Voce esta com obesidade morbida.')

# 45 fala o computador jogar jokempo com voce. pedra papel e tesoura.
import random

print("Vamos jogar Jokenpo!")
print("Escolha uma opção: \n 1. Pedra \n 2. Papel \n 3. Tesoura")
jogador = int(input("Sua escolha: "))
if jogador == 1:
    jogador_escolha = 'Pedra'
elif jogador == 2:
    jogador_escolha = 'Papel'
elif jogador == 3:
    jogador_escolha = 'Tesoura'
else:
    print("Opção inválida!")
    exit()
print("Você escolheu: ", jogador_escolha)
computador = random.randint(1, 3)
if computador == 1:
    computador_escolha = 'Pedra'
elif computador == 2:
    computador_escolha = 'Papel'
else:
    computador_escolha = 'Tesoura'
print("O computador escolheu: ", computador_escolha)
if jogador == computador:
    print("Empate!")
elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
    print("Você ganhou!")
else:
    print("Você perdeu!")
'''
# 44 que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento. a vista dinheiro/cheque 10% de desconto, a vista no cartao 5% de desconto, em ate 2x 
# no cartao preço normal, 3x ou mais no cartao 20% de juros
a = float(input('Informe o valor do produto: '))
print('-=' * 30)
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro / cheque 10%
[ 2 ] à vista no cartão 5%
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
b = int(input('Escolha a forma de pagamento e digite o numero especifico: '))
if b == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(a - (a * 0.10)))
elif b == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(a - (a * 0.05)))
elif b == 3:
    c = int(input('Em quantas quer fazer? Em 1x ou 2x? '))
    if c == 1:
        print('O valor ficou em {}x R$ {:.2f}'.format(c, a))
    elif c == 2:
        print('O valor ficou em {}x R$ {:.2f}'.format(c, a / 2))
    else:
        print('Numero invalido')
elif b == 4:
    d = int(input('Em quantas x voce quer parcelar acima de 3x? '))
    if d >= 3:
        total = a + (a * 0.2)
        print('Numero invalido.')
        print('O valor ficou em {}x de R$ {}'.format(d, a / d))
    else:
        print('Numero invalido.')
else:
    print('Opção invalida')
