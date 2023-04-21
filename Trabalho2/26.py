num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = 0

if num1 < num2:
    for i in range(num1, num2+1):
        print(i)
        soma += i
else:
    for i in range(num2, num1+1):
        print(i)
        soma += i

print("A soma dos números é:", soma)