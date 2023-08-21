def aumentar(real=0, au=0, formato=False):
    resultado = real + (real * au/100)
    return resultado if formato == False else (moeda(resultado))

def dobro(real=0, formato=False):
    dobro = real * 2
    return dobro if formato == False else (moeda(dobro))

def metade(real=0, formato=False):
    metade = real / 2
    return metade if formato == False else (moeda(metade))

def diminuir(real=0, dimi=0, formato=False):
    resultado = real - (real * dimi/100)
    return resultado if formato == False else (moeda(resultado))

def moeda(preço=0, moeda ='R$'):
    return f'{moeda}{preço:>7.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxa=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)

    print(f'Preço analisado: \t{moeda(preço)}')     # \t é adicionar tabulação
    print(f'O dobro do preço é: \t{dobro(preço, True)}')
    print(f'A metade do preço é:  \t{metade(preço, True)}')
    print(f'Aumentando \t\t{aumentar(preço, taxaa, True)}')
    print(f'Diminuindo \t\t{diminuir(preço, taxa, True)}')
    print('-' * 40)