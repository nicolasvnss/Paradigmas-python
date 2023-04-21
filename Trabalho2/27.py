num = int(input("Digite um número inteiro entre 1 e 10 para gerar a tabuada: "))

if num < 1 or num > 10:
    print("Número inválido. Por favor, digite um número entre 1 e 10.")
else:
    print("Tabuada de", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
