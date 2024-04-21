def calcular_preco_final(valor, estado):
    if estado == "MG":
        imposto = 0.07
    elif estado == "SP":
        imposto = 0.12
    elif estado == "RJ":
        imposto = 0.15
    elif estado == "MS":
        imposto = 0.08
    else:
        print("Estado inválido.")
        return None
    
    preco_final = valor * (1 + imposto)
    return preco_final

def main():
    valor = float(input("Digite o valor do produto: R$ "))
    estado = input("Digite o estado de destino (MG, SP, RJ, MS): ").upper()
    
    preco_final = calcular_preco_final(valor, estado)
    if preco_final is not None:
        print("O preço final do produto no estado de {} é R$ {:.2f}".format(estado, preco_final))

if __name__ == "__main__":
    main()
