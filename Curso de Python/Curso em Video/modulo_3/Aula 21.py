'''
# ---------- INTERACTIVE HELP ------------------
# help()  # rodando acessa qualquer funçção que tem no python 
# help(print)

# ------------ docstrings ----------------
def contador(i, f, p):
    """Faz uma contagem e mostra na tela:
        i (_type_): Inicio da contagem
        f (_type_): Fim da contagem
        p (_type_): Passo da contagem
        retorn:     Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)

# ----------------------- PARAMETROS OPCIONAIS --------------
def somar(a=0, b=0, c=0):   # como pode nao ter o valor de c, coloca =0 para que se nao tem o valor ele vale 0 #o nome desse c=0 é parametro opcional
    """_summary_

    Args:
        a (int, optional): _description_. Defaults to 0.
        b (int, optional): _description_. Defaults to 0.
        c (int, optional): _description_. Defaults to 0.
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 5)     # nao tem o valor se c
somar(c=3, b=5)

# ----------------------- ESCOPO DE VARIAVEIS --------------
# Escopo global é um valor de uma variavel fora (a=5) do def que ela vale tambem dentro do def (a=5).
# Escopo local é um valor de uma variavel que foi criada dentro do parametro def (b=5) que so vale dentro dele.
# para substituir a local pela global, tneho que escrever "global" logo abaixo de def

# ----------------------- RETORNO DE VALORES --------------
# return = faz a chamada e retorna o resultados
def somar(a=0, b=0, c=0):
    s = a + b + c
    # print(f'A soma vale {s}') o print foi removido para colocar o return
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(3, 5)
print(f'Os resultados forma {r1}, {r2} e {r3}')

# criar o fatorial de um numero
def fatorial(num = 1):
    f = 1
    for c in range(m, 0, -1):
        f *= c
    return f

# primeira opção / n = int(input('Digite um numero: '))
# primeira opção / print(f'O fatorial de {n} é igual é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

# programa principal
num = int(input('Digite um numero: '))
if par(num):
    print('É par! ')
else:
    print('Não é Par! ')
'''