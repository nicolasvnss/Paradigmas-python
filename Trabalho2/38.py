preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o primeiro produto, que custa R$ {:.2f}".format(preco1))
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o segundo produto, que custa R$ {:.2f}".format(preco2))
else:
    print("Você deve comprar o terceiro produto, que custa R$ {:.2f}".format(preco3))
