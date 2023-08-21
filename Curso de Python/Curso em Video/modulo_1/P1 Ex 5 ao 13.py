'''
# 5 Faça um programa que leia um numero inteiro e mostre na tela o seu 
# sucessor e seu antecessor
n = int(input('Insira um numero: '))
suc = 1+n
ant = n-1
print('O Sucessor é {} e o Antecessor é {}'.format(suc, ant))

# 6 leia um numero que mostre o dobro, triplo e raiz quadrada
n = int(input('Coloque um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro é {}, o Triplo é {} e a Raiz quadrada é {:.2f}'.format(d,t,r))

# 7 que leia duas notas de um aluno, calcule e mostre a media
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1+n2)/24
print('A media é {}'.format(m))

# 8 leia o valor em metros e exiba convertido em centimentros e milimetros
n = float(input('Insira a medida em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('O valor vale: \n{}km; \n{}hm; \n{}dam; \n{}m; \n{}dm; \n{}cm; \n{}mm.'.format(km,hm,dam,n,dm,cm,mm))

# 9 que leia um numero inteiro e mostre na tela a seua tabuada
n = int(input('Insira um numero: '))
print('-'*12)
print('{} x {:2} = {}'.format(n, 1, (n*1)))
print('{} x {:2} = {}'.format(n, 2, (n*2)))
print('{} x {:2} = {}'.format(n, 3, (n*3)))
print('{} x {:2} = {}'.format(n, 4, (n*4)))
print('{} x {:2} = {}'.format(n, 5, (n*5)))
print('{} x {:2} = {}'.format(n, 6, (n*6)))
print('{} x {:2} = {}'.format(n, 7, (n*7)))
print('{} x {:2} = {}'.format(n, 8, (n*8)))
print('{} x {:2} = {}'.format(n, 9, (n*9)))
print('{} x {:2} = {}'.format(n, 10, (n*10)))
print('-'*12)

# 10 leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares 
# pode comprar $3,27
n = float(input('Informe quanto tem na carteira em R$: '))
tx = n/3.27
print('Você pode comprar ${:.2f} dolares'.format(tx))

# 11 leia a largura e altura de uma parede em metros, calcule sua 
# area e a quantidade de tinta necessario para pinta-la, sabendo 
# que cada litro de tinta pinta uma area de 2m².
l = float(input('Informe a largura em m: '))
a = float(input('Informe a altura em m: '))
mq = l*a
print('Sua parede possui {:.2f}m² e precisará de {:.2f}L de tintas.'.format(mq,mq/2))

# 12 leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Informe o preço do produto: '))
t = p * 0.05
print('O valor possui um desconto 5%, ficando R$ {:.2f} '.format(p-t))

# 13 leia o salario de um funcionario que mostra 15% de aumento
s = float(input('Informe teu salario: '))
a = s * 0.15
print('O salario teve um reajuste de 15%, ficando R${:.2f}'.format(s+a))

# 14 leia a temperatura em graus celcius e transforma em fahrenheit
c = float(input('Qual a temperatura em º?: '))
f = ((9*c)/5)+32
print('A temperatura é {}f'.format(f))

# 15 Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a 
# pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Qual o quilometro percorrido? '))
dia = int(input("Quantos dias alugados? "))
vdiario = 60 * dia
vkm = km * 0.15
print('O valor do aluguel é {} e valor do km total é {}'.format(vdiario, vkm))
'''