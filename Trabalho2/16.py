while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Valor inválido. Por favor, digite novamente.")
    else:
        print(f"Nota digitada: {nota}")
        break
