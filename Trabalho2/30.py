n = int(input("Digite o valor de n: "))

fibonacci = [1, 1]

while len(fibonacci) < n:
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)

print("Série de Fibonacci até o {}º termo:".format(n))
print(fibonacci)
