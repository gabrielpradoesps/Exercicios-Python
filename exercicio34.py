mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O mês {mes} tem 29 dias no ano de {ano}.")
    else:
        print(f"O mês {mes} tem 28 dias no ano de {ano}.")

elif mes in [4, 6, 9, 11]:
    print(f"O mês {mes} tem 30 dias no ano de {ano}.")

elif mes in [1, 3, 5, 7, 8, 10, 12]:
    print(f"O mês {mes} tem 31 dias no ano de {ano}.")

else:
    print("Mês inválido.")