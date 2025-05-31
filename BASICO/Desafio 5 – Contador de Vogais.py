print('Ola, seja bem-vindo')

vogais = 'aeiou'
quantidade = 0
frase = input('Digite uma Frase: ')

for letra in frase:
    if letra.lower() in vogais:
        quantidade += 1

print(f"Ha {quantidade} vogais na Frase enviada")
