def imprime():
    print("Função")

imprime()
#com parametro
def imprime(n):
    print(n)

imprime("autodescritivo")
#com retorno
def potencia(n):
    return n * n

x = potencia(5)
print(x)
#com valor default
def intervalo(inic=1,fim=3):
    for n in range(inic, fim+1):
        print(n)

x = intervalo(1,3)
y = intervalo()