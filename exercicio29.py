
lado1 = float(input("Digite o tamanho do lado 1: "))
lado2 = float(input("Digite o tamanho do lado 2: "))
lado3 = float(input("Digite o tamanho do lado 3: "))

if (
    (lado1 + lado2 > lado3)
    and (lado1 + lado3 > lado2)
    and (lado2 + lado3 > lado1)
):
  print("Os valores formam um triângulo!")


  if lado1 == lado2 == lado3:
    print("Tipo: Triângulo Equilátero (três lados iguais).")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Tipo: Triângulo Isósceles (dois lados iguais).")
  else:
    print("Tipo: Triângulo Escaleno (três lados diferentes).")
else:
  print("Os valores informados NÃO podem formar um triângulo.")
