'''
a = 2
b = 3
soma = a + b
print(soma)
a = 4
b = 5
soma = a + b
print(soma)
a = 6
b = 6
soma = a + b
print(soma)

def soma(a,b):
    s = a + b
    print(s)

soma(2, 5)
soma(6, 54)
soma(66, 77)

def numeros(* num):
    tamanho = len(num)
    print(f'Recbi os valores {num} e são ao todo {tamanho} numeros.')

numeros(1, 2, 5, 4, 9)
numeros(13, 44, 52, 34, 59, 154)
numeros(1, 1, 2)
# ---------------------------------- lista --------
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6, 4, 4, 2, 6, 10]
dobra(valores)
print(valores)
'''
# ------ desempacotamento ----------
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(6, 7, 110, 125)

