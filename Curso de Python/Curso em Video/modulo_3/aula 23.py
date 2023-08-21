'''
try:   # tente fazer (operação)
    a = int(input('Numerador: '))
    b = int(input('Denomindador: '))
    r = a / b
except (ValueError, TypeError):   # falhou pode ter varios 
    print(f'Tivemos um problema com os dados digitados')
except ZeroDivisionError:
    print('Nao é possivel dividir por zero')
else:
    print(f'O resultador é {r}')
finally:    # certo/falha
    print('Volte sempre! muito obrigado')

# 113 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
#  digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a 
# mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n

#def leiaFloat(msg):

n = leiaInt('Digite um inteiro: ')
#m = leiaFloat('Digite um real')
print(f'Voce acabou de digitar o numero {n}')

# 114 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests

def verificar_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O site {url} está acessível.")
        else:
            print(f"O site {url} não está acessível. Código de status: {response.status_code}")
    except requests.ConnectionError:
        print(f"O site {url} não está acessível. Não foi possível estabelecer uma conexão.")

verificar_site("http://pudim.com.br/")
# ---------------------------------- ou --------------------------------

import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta acesseivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
'''
# 115 Vamos criar um menu em Python, usando modularização.
