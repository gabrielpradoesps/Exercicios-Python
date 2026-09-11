imovel = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o valor do salário: "))
prazo = int(input("Digite o prazo em anos: "))

prestacao = imovel / (prazo * 12)
limite = salario * 0.3
if prestacao <= limite:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação: R${prestacao:.2f}")
    print(f"Limite: R${limite:.2f}")

else:
    print("Empréstimo negado!")
    print(f"Valor da prestação: R${prestacao:.2f}")
    print(f"Limite: R${limite:.2f}")