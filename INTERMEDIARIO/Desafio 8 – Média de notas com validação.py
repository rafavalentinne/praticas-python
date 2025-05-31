def calcular_media():
    notas = []
    for i in range(3):
        while True:
            try:
                nota_str = input(f"Digite a {i+1}ª nota do aluno (entre 0 e 10): ")
                nota = float(nota_str)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Por favor, tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    calcular_media()



"""
CONTRIBUICOES ABAIXO
"""
