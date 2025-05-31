print('Ola, seja bem-vindo')

num = int(input('Digite um numero: '))
numero = []

for i in range(1, num+1):
    print(i)
    numero.append(i)

print(sum(numero))


