'''
num = [2, 5, 4, 9, 11,]
num[3] = 4         # substitui o n que esta na ordem 3 pelo numero 4
num.append(7)      # acrescenta o 7 ao final da lista
num.sort()          # organiza os numero em ordem crescente
num.sort(reverse=True)  # Organiza os numeros em ordem decrescente
num.insert(2, 2)       # insere o 2 na segunda posição
num.remove(2)          #remove o primeiro 2 encontrado na lista
num.pop(2)              #remove o valor que esta na posição 2   
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos. ')

valores = [] # lista vazia, ou valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final lista')

a = [2, 3, 4, 7]
b = a[:]      # cria uma copia de a em b
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])     # mostra apenas pedro
print(dados[1])     # mostra apenas 25

pessoas =list()
pessoas.append(dados[:]) # insere a lista dados (2 possiçoes), na posição 0 de pessoas. Uma lista dentro da outra

teste = []
teste.append('Gustavo')         # adiciona gustavo na lista teste
teste.append(40)                # adiciona 40 na lista teste

galera = list()                 # cria uma lista galera
# galera.append(teste)            # cria ligação entre as duas lista ( o que muda em uma, muda em outra)
galera.append(teste[:])         # aqui criei uma copia de galera em teste
teste[0] = 'Maria'          # dicionei maria a lista teste
teste[1] = 22               #adicionei 22 a lista teste
galera.append(teste[:])    
print(galera),

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][0])  # pega e mostra so o joao, pois esta na posiçao 0,0
for p in galera:
    print(p[0])     # motra todos na posição 0 (os nomes)
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = []
dado = []
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])   #copia do dado 
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior de idade e {totmen} menor de idade.')
'''