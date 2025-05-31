"""
Crie uma função que verifica se uma palavra é um palíndromo (lida ao contrário é igual).

Exemplos:

arara → ✅

python → ❌

"""

def palindromo(palavra):
    palavra.lower().replace(" ", "")
    palavra_reversa = palavra[::-1]
    if palavra == palavra_reversa:
        return "Palíndromo"
    else:
        return "Nao é palíndromo"

palavra = input('Digite uma palavra: ')

print(palindromo(palavra))

