num1 = 1
num2 = 1
s = 1
while num1 < 98:
    num1 += 2
    num2 += 1
    s += num1/num2
    print(num1, num2, s)

def first():
    return("bruninho")

print(first())

def saudacao(nome, saudacao="Ola"):
    print(nome, saudacao)

saudacao("bidu")
saudacao("cap", "Oi")

def operacao_a():
    resultado = 7 * 3 - 5
    print("O resultado da operação é:", resultado)

resultado = 5
operacao_a()
print("resultado =", resultado)