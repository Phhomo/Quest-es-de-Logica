def tipo_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Os valores fornecidos não formam um triângulo."
    elif a == b == c:
        return "Os valores formam um triângulo equilátero."
    elif a == b or a == c or b == c:
        return "Os valores formam um triângulo isósceles."
    else:
        return "Os valores formam um triângulo escaleno."

def main():
    a = float(input("Digite o comprimento do lado A do triângulo: "))
    b = float(input("Digite o comprimento do lado B do triângulo: "))
    c = float(input("Digite o comprimento do lado C do triângulo: "))
    
    resultado = tipo_triangulo(a, b, c)
    print(resultado)

if __name__ == "__main__":
    main()
