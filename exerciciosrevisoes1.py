def diastotais():
    anos = int(input("Digite o ano de nascimento"))
    mes = int(input("Digite o numero do mes de nascimento"))
    while (12 > mes < 0):
        mes = int(input("Digite o numero do mes de nascimento"))
    dia = int(input("Digite o dia do nascimento"))
    anos2 = int(input("Digite o ano da data atual"))
    mes2 = int(input("Digite o numero do mes da data atual"))
    while (12 > mes2 < 0):
        mes2 = int(input("Digite o numero do mes da data atual"))
    dia2 = int(input("Digite o dia atual"))
    ano = (anos2 - anos) * 365
    mes3 = (mes2 - mes) * 30
    ydias = (dia2 - dia)
    dias = (ano + mes3 + ydias)
    print("Você viveu:", dias)

def primo():
        n = int(input("Digite um numero"))
        if n > 8:
            if (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
                print("primo")
            else:
                print("nao primo")
        else:
            if (n == 2) or (n == 3) or (n == 5) or (n == 7):
                print("primo")
            else:
                print("nao primo")
r = 1   
while r == 1:
    primo()
    r = 0
    r = int(input("Se quiser digitar mais numeros digite 1"))

def calculoS():
    num = int(input("Digite um numero"))
    s = 0
    conta = 0
    while num > conta:
        conta += 1
        s = (conta*3) - 1
        print(s)
