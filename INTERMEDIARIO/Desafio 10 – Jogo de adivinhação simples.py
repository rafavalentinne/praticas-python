"""
🎲 Desafio 10 – Jogo de adivinhação simples
O programa deve gerar um número aleatório de 1 a 10 e pedir para o usuário adivinhar.
Diga se ele acertou ou errou, e quantas tentativas ele preciso

"""
import random

numero_aleatorio = random.randint(1, 10)

numero_escolhido = int(input("Adivinha o Número, de 1 a 10: "))

if numero_escolhido == numero_aleatorio:
    print("ACERTO!!!")

else:
    print("ERROU!!!")