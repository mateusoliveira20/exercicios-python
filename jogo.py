inter = int(input())
gremio = int(input())
vitorias = 0
vitorias1 = 0
empate = 0
while inter >= 0 and gremio >=0 :
    if inter > gremio:
        vitorias += 1  
    elif gremio > inter:
        vitorias1 += 1
    else:
        empate += 1
    while True:
        x = input("quer continuar")
        if x == s:
            break
    while grenal == s:
        break
    inter = int(input())
    remio = int(input())
total = vitorias+vitorias1+empate
print("%d grenais" % (total))
print("inter: %d" % (vitorias))
print("gramio: %d" % (vitorias1))
print("empates: %d" % (empate))
