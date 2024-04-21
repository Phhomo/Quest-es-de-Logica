import math

numero = float(input("Digite um número: "))
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("O número é inválido porque é negativo.")
