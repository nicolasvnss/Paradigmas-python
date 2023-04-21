altura = float(input("Digite a altura da pessoa em metros: "))
genero = input("Digite o gênero da pessoa (M ou F): ")

if genero == "M":
    peso_ideal = (72.7 * altura) - 58
elif genero == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Gênero inválido!")
    peso_ideal = None

if peso_ideal is not None:
    print("O peso ideal para uma pessoa com altura", altura, "e gênero", genero, "é:", peso_ideal, "kg")
