numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = max(numeros)
print(f"O maior número é {maior}.")
