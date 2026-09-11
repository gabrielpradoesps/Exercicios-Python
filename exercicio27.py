peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'{imc:.2f}')
    print("ABAIXO DA FAIXA")

elif imc >= 18.5 and imc < 25:
    print(f'{imc:.2f}')
    print("FAIXA NORMAL")

elif imc >= 25 and imc < 30:
    print(f'{imc:.2f}')
    print("ACIMA DA FAIXA")

else:
    print(f'{imc:.2f}')
    print("FAIXA ELEVADA")