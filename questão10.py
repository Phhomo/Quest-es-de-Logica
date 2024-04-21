def soma_algarismos(numero):
    soma = 0
    
    for digito in str(numero):
        soma += int(digito)
    
    return soma

def main():
    numero = int(input("Digite um número inteiro maior do que zero: "))
    
    if numero <= 0:
        print("Número inválido")
    else:
        print("A soma dos algarismos é:", soma_algarismos(numero))

if __name__ == "__main__":
    main()
