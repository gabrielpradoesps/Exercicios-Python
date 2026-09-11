idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante? (s/n): ")

ingresso = 30
meia_entrada = ingresso / 2

if idade <= 12 or idade >= 60 or estudante == "s":
    print(f"O valor do ingresso é R${meia_entrada:.2f}.")
else:
    print(f"O valor do ingresso é R${ingresso:.2f}.")


