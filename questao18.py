def verifica_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "O número é divisível por 3 e por 5."
    elif numero % 3 == 0:
        return "O número é divisível por 3, mas não por 5."
    elif numero % 5 == 0:
        return "O número é divisível por 5, mas não por 3."
    else:
        return "O número não é divisível por 3 nem por 5."

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = verifica_divisibilidade(numero)
    print(resultado)

if __name__ == "__main__":
    main()
