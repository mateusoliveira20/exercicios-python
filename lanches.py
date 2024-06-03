cod,quant = input().split(" ")
cod,quant = int(cod),int(quant)
if cod == 1:
    total = quant*4
    print("Total: R$ %.2f" % (total))
elif cod == 2:
    total = quant*4.50
    print("Total: R$ %.2f" % (total))
elif cod == 3:
    total = quant*5
    print("Total: R$ %.2f" % (total))
elif cod == 4:
    total = quant*2
    print("Total: R$ %.2f" % (total))
elif cod == 5:
    total = quant*1.50
	print("Total: R$ %.2f" % (total))
