base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(expoente):
    resultado *= base

print(base, "elevado a", expoente, "é igual a", resultado)
