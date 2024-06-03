cod = int(input())
quant = int(input())
total = int(input())
if cod == 1:
    total == quant * 4
elif cod == 2:
    total == quant*4.50
elif cod == 3:
    total == quant*5
elif cod == 4:
    total == quant*2
elif cod == 5:
    total == quant*1.50
print("TOTAL = R$ %d" % (total))
