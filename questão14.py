def obter_dia_semana(numero):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    return dias_semana.get(numero, "Número inválido")

def main():
    numero = int(input("Digite um número entre 1 e 7: "))
    dia_semana = obter_dia_semana(numero)
    print("Dia da semana correspondente:", dia_semana)

if __name__ == "__main__":
    main()
