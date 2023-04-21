while True:
    nome = input("Digite o seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    print("Nome inválido. Deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite a sua idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    print("Idade inválida. Deve estar entre 0 e 150 anos.")

while True:
    salario = float(input("Digite o seu salário (maior que zero): "))
    if salario > 0:
        break
    print("Salário inválido. Deve ser maior que zero.")

while True:
    sexo = input("Digite o seu sexo (f/m): ")
    if sexo.lower() in ['f', 'm']:
        break
    print("Sexo inválido. Deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite o seu estado civil (s/c/v/d): ")
    if estado_civil.lower() in ['s', 'c', 'v', 'd']:
        break
    print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
