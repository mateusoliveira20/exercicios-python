n = int(input())
horas = n//3600
minuto = (n % 3600)//60
segundo = (n % 3600) % 60
print("%d:%d:%d" % (horas,minuto,segundo))
