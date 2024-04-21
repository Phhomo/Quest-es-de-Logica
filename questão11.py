import math

def main():
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 0:
        print("Número inválido")
    else:
        resultado = math.log(numero)
        print("O logaritmo do número é:", resultado)

if __name__ == "__main__":
    main()
