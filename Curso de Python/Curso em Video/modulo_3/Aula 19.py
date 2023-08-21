
pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 98.5      #adicionar peso no dicionario

#for k in pessoas.keys():
#    print(k)
#
#for k in pessoas.values():
#    print(k)
#
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
#
#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uF': 'Sao Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[1]['sigla'])
#
#
#estado = dict()
#brasil = list()
#
#for c in range(0, 3):
#    estado['uf'] = str(input('Unidade Federativa: '))
#    estado['sigla'] = str(input('Sigla do Estado: '))
#    brasil.append(estado.copy())    #.copy copia um dicionario
#for e in brasil:
#    for k, v in e.items():
#        print(f'O campo {k} tem o valor {v}.')