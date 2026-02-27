segundo = int(input("Digite quantos segundos tem"))
horas = segundo // 3600
minutos = (segundo // 60) - (horas * 60)
segundos = segundo % 60
print(horas,"h", minutos, "m", segundos, "s")
