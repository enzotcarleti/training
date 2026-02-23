comprar = int(input("Digite o valor da compra"))
pagar = int(input("Digite o valor do pagamento"))
troco = pagar - comprar
cem = troco // 100
troco2 = troco - (100 * cem)
cinquenta = troco2 // 50
troco3 = troco2 - (50 * cinquenta)
vinte = troco3 // 20
troco4 = troco3 - (20 * vinte)
dez = troco4 // 10
troco5 = troco4 - (10 * dez)
cinco = troco5 // 5
troco6 = troco5 - (5 * cinco)
dos = troco6 // 2
troco7 = troco6 - (2 * dos)
um = troco7 // 1
print("Valor do troco total:", troco)
print("Notas de cem:", cem)
print("Notas de cinquenta", cinquenta)
print("Notas de vinte", vinte)
print("Notas de dez", dez)
print("Notas de cinco", cinco)
print("Notas de dois", dos)
print("Moedas de um real", um)
