com = float(input("Valor da compra: "))
opcao = int(input("Qual é a forma de pagamento? "))

if opcao == 1:
    total = com - (com * 10 / 100)
    print("Valor da compra: %.2f" % total)
elif opcao == 2:
    total = com - (com * 5 / 100)
    print("Valor da compra: %.2f" % total)
elif opcao == 3:
    total = com
    parcela = total / 2
    print("Preço total: %.2f, Parcela: %.2f" % (total, parcela))
elif opcao == 4:
    total = com + (com * 20 / 100)
    print("Valor da compra: %.2f" % total)
