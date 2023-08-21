
chave = input('Digite sua senha para ser criptografada: ')

senha = ""

for letra in chave:
    if letra in "Aa": senha += "1" 
    if letra in "Bb": senha += "8" 
    if letra in "Cc": senha += "%" 
    if letra in "Oo": senha += "@" 
    if letra in "1": senha += "!" 
    if letra in "Ss": senha += "$" 
    if letra in "Uu": senha += "+" 
    else: senha += letra

print(senha)