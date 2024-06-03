nome = input("digite seu nome:")
salariofixo = float(input("seu salario fixo:"))
totalvendas = float(input("total de vendas:"))
s = totalvendas*15 /100
total = salariofixo+s
print("TOTAL = R$ %.2f" % (total))
