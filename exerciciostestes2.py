def c():
    string = 'capedaoraecarleti'

    cont = 0
    for i in range(len(string)):
        if string[i] == 'c':
            cont += 1

    for i in range(len(string)):
        if string[i] != 'c':
            print(string[i], end="")
        else: 
            print(f"d",end='')

def a():
    string1 = 'eduardo'
    string2 = 'colmati'

    string3 = string1 +string2

    print(len(string3) - 1)
    print(string3[0], string3[-1])

def b():
    idade_menor = 0
    idade_maior = 0
    nome_menor = ''
    nome_maior = ''
    idade = 0
    while idade >= 0:
        idade = int(input("Idade: "))
        nome = input("digite o nome: ")
        nome = nome.split(" ")[0]
        if idade < idade_menor and idade >= 0:
            idade_menor = idade
            nome_menor = nome

        if idade > idade_maior:
            idade_maior = idade
            nome_maior = nome

    print(f"idade menor: {idade_menor}, idade maior: {idade_maior}, nome menor: {nome_menor} nome maior: {nome_maior}")


p = input("Palavra: ")
for i in range(len(p)):
    s = -1
    print(p[s - i], end="")
