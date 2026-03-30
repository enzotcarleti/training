# def ex1():
#     x = int(input("Digite o numero"))
#     print(x - 1, x + 1)

# ex1()

# def num1():
#     x = int(input("Digite um numero"))
#     return x
# def num2():
#     y = num1()
#     w = num1()
#     v = num1()
#     return (y + w + v)
# def num3(): 
#     z = num1()
#     return z

# a = num2()
# b = num1()
# c = num3()
# print (a + b + c)

def ex3():
    num1 = int(input("Digite o numero"))
    num2 = int(input("Digite o segundo numero"))
    num3 = 0
    if num1 > num2 and num2 % 2 == 1:
        num2 -= 1
    if num2 > num1 and num1 % 2 == 1:
        num1 -= 1
    while num1 > num2 and num2 % 2 == 0:
        num2 += 2
        print(num2)
    while num2 > num1 and num1 % 2 == 0:
        num1 += 2
        print(num1)

def ex4():
    num1 = int(input("Digite o numero"))
    num2 = int(input("Digite o segundo numero"))
    num3 = 0
    if num1 > num2:
        num2 -= 1
    while num1 > num2:
        num2 += 1
        num3 += num2
        print(num2, num3)
    if num2 > num1:
        num1 -= 1
    while num2 > num1:
        num1 += 1
        num3 += num1
        print(num1, num3)

ex4()