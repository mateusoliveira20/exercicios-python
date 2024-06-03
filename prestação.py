casa = float(input("valor da casa "))
salario = float(input("valor do salario "))
anos = int(input("quantos de emprestimo "))
prestação = casa / (anos * 12)
mini = salario *30 / 100
if prestação <= mini:
    print("voce tem permisao")
else:
    print("acesso negado")
