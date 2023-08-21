
#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  #TUPLA sao imutaveis
#print(lanche)
#print(lanche[0])
#print(lanche[1:3])
#print(lanche[2:])
#print(lanche[:2])
#print(lanche[-2])
#print(lanche[:-2])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in enumerate(lanche):    # enumerate mostra a posição dentro de lanche
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche))
'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):    # Iteração uma opçao
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) # COLOCA NA ORDEM ALFABETICA

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('gustavo', 39, 'M', 99.98) # tupla pode ter nome e numero
del(pessoa)  # apaga da memoria
print(pessoa)
'''