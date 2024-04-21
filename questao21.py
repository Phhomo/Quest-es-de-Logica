def eh_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

def main():
    ano = int(input("Digite um ano: "))
    
    if eh_bissexto(ano):
        print("O ano {} é bissexto.".format(ano))
    else:
        print("O ano {} não é bissexto.".format(ano))

if __name__ == "__main__":
    main()
