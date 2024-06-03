valor = input("valor da compra: ")
valor = float(valor)
opcao = input("opção de pagamento (1,2 ou 3): ")
opcao = int(opcao)
if opcao == 1:
    total = valor*5/100
    des = valor-total
    print("desconto %.2f" % (des))
elif opcao == 2:
    total = valor/5
    print("5x %.2f" % (total))
elif opcao == 3:
    total = valor*10/100
    aum = total+valor
    print("aumento de %.2f" % (aum))
print("boa noite")
