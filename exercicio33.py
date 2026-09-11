numero = int(input("Digite um número inteiro: "))

segunda = 1
terca = 2
quarta = 3
quinta = 4
sexta = 5
sabado = 6
domingo = 7

if numero == segunda:
    print("O número corresponde a Segunda-feira.")
elif numero == terca:
    print("O número corresponde a Terça-feira.")
elif numero == quarta:
    print("O número corresponde a Quarta-feira.")
elif numero == quinta:
    print("O número corresponde a Quinta-feira.")
elif numero == sexta:
    print("O número corresponde a Sexta-feira.")
elif numero == sabado:
    print("O número corresponde a Sábado.")
elif numero == domingo:
    print("O número corresponde a Domingo.")
else:
    print("O número não corresponde a nenhum dia da semana.")