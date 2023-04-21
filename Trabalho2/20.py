while True:
    try:
        populacao_a = int(input("Informe a população da cidade A: "))
        taxa_a = float(input("Informe a taxa de crescimento da cidade A (%): ")) / 100
        populacao_b = int(input("Informe a população da cidade B: "))
        taxa_b = float(input("Informe a taxa de crescimento da cidade B (%): ")) / 100

        anos = 0
        while populacao_a <= populacao_b:
            populacao_a += int(populacao_a * taxa_a)
            populacao_b += int(populacao_b * taxa_b)
            anos += 1
        
        print(f"Levará {anos} anos para a população da cidade A ultrapassar a população da cidade B.")
        
        repetir = input("Deseja repetir a operação? (s/n): ")
        if repetir.lower() != "s":
            break

    except ValueError:
        print("Valor inválido. Tente novamente.")
