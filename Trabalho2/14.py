peso = float(input("Digite o peso dos peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Peso de peixes excedente: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("Peso dentro do limite permitido.")
