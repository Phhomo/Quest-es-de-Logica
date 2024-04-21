def calcular_area_trapezio(base_maior, base_menor, altura):
    if base_maior <= 0 or base_menor <= 0:
        print("As bases devem ser números maiores que zero.")
        return None
    
    area = ((base_maior + base_menor) * altura) / 2
    return area

def main():
    base_maior = float(input("Digite o valor da base maior do trapézio: "))
    base_menor = float(input("Digite o valor da base menor do trapézio: "))
    altura = float(input("Digite o valor da altura do trapézio: "))

    area = calcular_area_trapezio(base_maior, base_menor, altura)

    if area is not None:
        print("A área do trapézio é:", area)

if __name__ == "__main__":
    main()
