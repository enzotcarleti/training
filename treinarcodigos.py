def a():
    x = []
    m3 = 0
    n = int(input("Numero de elementos até 20: "))
    while n > 20:
        print("Numero de elementos deve ser menor ou igual a 20.")
        n = int(input("Numero de elementos até 20: "))
    for i in range(n):
        dado = int(input("Fale o numero " + str(i + 1) + ": "))
        x.append(dado)

    for i in range(len(x)):
        if x[i] % 3 == 0:
            m3 += 1

    print(x)
    print(m3)

def a2():
    x = 0
    par = []
    impar = []
    while x >= 0:
        x = int(input("Digite um numero: "))
        if x % 2 == 0 and x >= 0:
            par.append(x)
        elif x % 2 != 0 and x >= 0:
            impar.append(x)

    print("Numeros pares:", par)
    print("Numeros impares:", impar)

def b():
    x = []
    maiornu = 0
    menornu = 0
    maiorpos = 0
    menorpos = 0
    
    n = int(input("Numero de elementos até 10: "))
    while n > 10:
            print("Numero de elementos deve ser menor ou igual a 10.")
            n = int(input("Numero de elementos até 10: "))
    for i in range(n):
        numero = int(input("Fale o numero " + str(i + 1) + ": "))
        x.append(numero)

    for i in range(len(x)):
        if x[i] > maiornu:
            maiornu = x[i]
            maiorpos = i + 1
        if x[i] < menornu:
            menornu = x[i]
            menorpos = i + 1

    print(x)
    print("Maior numero:", maiornu, "na posicao", maiorpos)
    print("Menor numero:", menornu, "na posicao", menorpos)


livros = {
1001: ["Dom Casmurro", 1, "Machado de Assis", 35.90],
1002: ["O Senhor dos Anéis", 1, "J.R.R. Tolkien", 89.90],
1003: ["1984", 1, "George Orwell", 42.50],
1004: ["Fundação", 1, "Isaac Asimov", 48.00],
1005: ["O Hobbit", 2, ["J.R.R. Tolkien", "Christopher Tolkien"], 54.90],
}

def buscar_livros():
    livro = input("Titulo do livro")

    for id, i in livros.items():
        if i[0] == livro:
            print("id:", id)
            print("Titulo:", i[0])
            print("Numero de Autores:", i[1])
            print("Autor(es):", i[2])
            print("Preço:",i[3])
            return

    print("Não foi achado")

def buscar_livros_porid():
    livro = int(input("Id do livro"))

    for id, i in livros.items():
        if id == livro:
            print("id:", id)
            print("Titulo:", i[0])
            print("Numero de Autores:", i[1])
            print("Autor(es):", i[2])
            print("Preço:",i[3])
            return

    print("Não foi achado")

def livroscaros():
    for id, i in livros.items():
        if i[3] > 50:
            print("id:", id)
            print("Titulo:", i[0])
            print("Numero de Autores:", i[1])
            print("Autor(es):", i[2])
            print("Preço:",i[3])

livroscaros()
            