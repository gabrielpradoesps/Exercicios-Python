numero = float(input("Digite um número: "))
intervalo = (10, 20)

if intervalo[0] <= numero <= intervalo[1]:
    print(f"O número {numero} está dentro do intervalo {intervalo}.")
else:
    print(f"O número {numero} não está dentro do intervalo {intervalo}.")