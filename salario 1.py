sal = float(input())
if (sal>=0 and sal<=400.00):
    per = 15
    aum = sal*per/100
    total = sal + aum
    print("Novo salario: %.2f" % (total))
    print("Reajuste ganho: %.2f" % (aum))
    print("Em percentual: %.0f %%" % (per))
elif (sal>=400.01 and sal<=800.00):
    per = 12
    aum = sal*per/100
    total = sal+aum
    print("Novo salario: %.2f" % (total))
    print("Reajuste ganho: %.2f" % (aum))
    print("Em percentual: %.0f %%" % (per))
elif (sal>=800.01 and sal<=1200.00):
    per = 10
    aum = sal*per/100
    total = sal+aum
    print("Novo salario: %.2f" % (total))
    print("Reajuste ganho: %.2f" % (aum))
    print("Em percentual: %.0f %%" % (per))
elif (sal>=1200.01 and sal<=2000.00):
    per = 7
    aum = sal*per/100
    total = sal+aum
    print("Novo salario: %.2f" % (total))
    print("Reajuste ganho: %.2f" % (aum))
    print("Em percentual: %.0f %%" % (per))
elif (sal>2000):
    per = 4
    aum = sal*per/100
    total = sal+aum
    print("Novo salario: %.2f" % (total))
    print("Reajuste ganho: %.2f" % (aum))
    print("Em percentual: %.0f %%" % (per))
