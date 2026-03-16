num = int(input("Digite um numero"))
num2 = int(input("Digite um numero"))
num3 = int(input("Digite um numero"))
if num > num2 and num > num3:
    if num2 > num3:
        print(num3, num2, num)
    else:
        print(num2, num3, num)
else:
    if num2 > num and num2 > num3:
        if num3 > num:
            print(num, num3, num2)
        else:
            print(num3, num, num2)
    else:
        if num2 > num:
            print(num, num2, num3)
        else:
            print(num2, num, num3)
num = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
print("Selecione a operação: 1 para média, 2 para diferença do maior pro menor, 3 para multiplicar e 4 para dividir o primeiro pelo segundo")
seleciona = int(input("Digite um número de 1 a 4 para selecionar a operação"))
if seleciona == 1:
    print("média:", (num + num2)/2)
else:
    if seleciona == 2:
        if num > num2:
            print("diferença do maior para o menor:", num - num2)
        else:
            print("diferença do maior para o menor:", num2 - num)
    else:
        if seleciona == 3:
            print ("multiplicação dos números:", num * num2)
        else:
            if seleciona == 4:
                print("dividir primeiro pelo segundo numero:", num / num2)
            else:
                if seleciona > 4:
                    print("erro, número não deu certo")
x = 105
while x < 448:
  x = x + 7
  print(x)