salario = int(input("Digite o valor do seu salário: "))

porcentagem1 = 15
porcentagem2 = 10
porcentagem3 = 5

if salario == 1500:
    reajuste1 = salario * (1 + porcentagem1 / 100)
    print("O Reajuste do seu salário é: R$", reajuste1)

elif salario >= 1501 and salario <= 3000:
    reajuste2 = salario * (1 + porcentagem2 / 100)
    print("O Reajuste do seu salário é: R$", reajuste2)

else:
    reajuste3 = salario * (1 + porcentagem3 / 100)
    print("O Reajuste do seu salário é: R$", reajuste3)