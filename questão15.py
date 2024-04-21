def imprimir_mes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    if numero in meses:
        print(meses[numero])
    else:
        print("Número inválido. O número deve estar entre 1 e 12.")

def main():
    numero = int(input("Digite um número entre 1 e 12: "))
    imprimir_mes(numero)

if __name__ == "__main__":
    main()
