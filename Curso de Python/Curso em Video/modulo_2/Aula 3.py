'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vo digitou {} numeros pares e {} numeros impares!'.format(par, impar))
'''
def calcular_area(largura, altura):
    area = largura * altura
    return area

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = calcular_area(largura, altura)

print(f"A área do retângulo é {area}")