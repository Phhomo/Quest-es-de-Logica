def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def mostrar_menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da operação desejada (ou 's' para sair): ")

        if opcao == 's':
            print("Saindo do programa...")
            break

        if opcao in ['1', '2', '3', '4']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = soma(a, b)
                print("Resultado da soma:", resultado)
            elif opcao == '2':
                resultado = subtracao(a, b)
                print("Resultado da subtração:", resultado)
            elif opcao == '3':
                resultado = multiplicacao(a, b)
                print("Resultado da multiplicação:", resultado)
            elif opcao == '4':
                resultado = divisao(a, b)
                print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

if __name__ == "__main__":
    main()
