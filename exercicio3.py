# salario = int(input("Digite o salário"))
# if salario < 1500:
#     print("O salário teve aumento de 15% no total", salario * 1.15)
# else:
#     if (3000 > salario > 1500):
#         print("O salário teve aumento de 10% no total", salario * 1.10)
#     else:
#         print("O salário teve aumento de 5% no total", salario * 1.05)

lado = int(input("Digite o primeiro lado do triangulo"))
lado2 = int(input("Digite o segundo lado do triangulo"))
lado3 = int(input("Digite o terceiro lado do triangulo"))

if (lado - (lado2 + lado3)) < 0 and (lado2 - (lado + lado3)) < 0 and (lado3 - (lado + lado2)) < 0:
    if lado == lado2 == lado3:
        print("Equilátero")
    if lado == lado2 != lado3 or lado2 == lado3 != lado or lado == lado3 != lado2:
        print("Isósceles")
    if lado != lado2 != lado3:
        print("Escaleno")
else:
    print("erro")