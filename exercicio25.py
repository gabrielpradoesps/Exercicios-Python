preço = int(input("Digite o valor do produto: "))
porcentagem1 = 10
porcentagem2 = 5
porcentagem3 = 8

opc1 = "Dinheiro ou Pix"
opc2 = "Débito"
opc3 = "Crédito à vista"
opc4 ="Crédito parcelado"

print(opc1, "= opc1 \n", opc2, "= opc2 \n", opc3, "= opc3 \n", opc4, "= opc4")

formapag = input("Escolha a forma de pagamento: ")

if formapag == "opc1":
    desconto1 = preço * (1 - porcentagem1 / 100)
    print("Valor final: R$", desconto1)

elif formapag == "opc2":
    desconto2 = preço * (1 - porcentagem2 / 100)
    print("Valor final: R$", desconto2)

elif formapag == "opc3":
    print("Valor final: R$", preço)

else:
    desconto3 = preço * (1 + porcentagem3 / 100)
    print("Valor final: R$", desconto3)