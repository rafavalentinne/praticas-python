def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


numero = int(input("Digite um numero: "))

print(fatorial(numero))


"""
CONTRIBUICOES ABAIXO
"""
