def classificar_categoria(idade):
    if 5 <= idade <= 7:
        categoria = "Infantil A"
    elif 8 <= idade <= 10:
        categoria = "Infantil B"
    elif 11 <= idade <= 13:
        categoria = "Juvenil A"
    elif 14 <= idade <= 17:
        categoria = "Juvenil B"
    else:
        categoria = "Sênior"
    return categoria

def main():
    idade = int(input("Digite a idade do atleta: "))
    categoria = classificar_categoria(idade)
    print("O atleta está na categoria:", categoria)

if __name__ == "__main__":
    main()
