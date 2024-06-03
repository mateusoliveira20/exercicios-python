nasc = int(input("nascimento"))
idade = 2023 - nasc
print(" voce tem %d anos" % (idade))
if idade <= 9:
    print("então voce esta na categoria mirim")
elif idade >=10 and idade<= 14 :
    print("então voce esta na categoria infantil")
elif idade >=15 and idade<=19:
    print("então voce esta na categoria junior")
elif idade >= 20 and idade<= 25:
    print("então voce esta na categoria senior")
else:
    print("então voce esta na categoria master")
