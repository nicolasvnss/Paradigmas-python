valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("Salário bruto: ({:.2f} * {:.2f}) \t: R$ {:.2f}".format(valor_hora, horas_trabalhadas, salario_bruto))
print("(-) IR ({:.2%}) \t\t\t\t: R$ {:.2f}".format(ir/salario_bruto, ir))
print("(-) INSS ({:.2%}) \t\t\t\t: R$ {:.2f}".format(inss/salario_bruto, inss))
print("(-) Sindicato ({:.2%}) \t\t\t: R$ {:.2f}".format(sindicato/salario_bruto, sindicato))
print("FGTS ({:.2%}) \t\t\t\t: R$ {:.2f}".format(0.11, fgts))
print("Total de descontos \t\t\t: R$ {:.2f}".format(total_descontos))
print("Salário Líquido \t\t\t\t: R$ {:.2f}".format(salario_liquido))
