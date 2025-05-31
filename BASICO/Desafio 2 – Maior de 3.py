print('Ola, seja bem-vindo')

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('numero 1 eh maior', numero1)
elif numero1 > numero2 and numero1 < numero3:
    print('numero 3 eh maior', numero3)
else:
    print('numero 2 eh maior', numero2)
