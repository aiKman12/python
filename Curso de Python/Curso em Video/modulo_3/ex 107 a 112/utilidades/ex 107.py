# 107 Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
import dado

valor = dado.leiaDinheiro('Digite o preço: R$ ')
dim = float(input(f'Quer diminuir quantos % de R$ {valor:.2f}? '))
aum = float(input(f'Quer aumentar quantos % de R$ {valor:.2f}? '))

moeda.resumo(valor)

# Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário

# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando 
# se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira 
# todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.