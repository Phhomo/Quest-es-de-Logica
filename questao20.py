def verificar_aposentadoria(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return True
    else:
        return False

def main():
    idade = int(input("Digite a idade do trabalhador: "))
    tempo_servico = int(input("Digite o tempo de serviço do trabalhador em anos: "))
    
    if verificar_aposentadoria(idade, tempo_servico):
        print("O trabalhador pode se aposentar.")
    else:
        print("O trabalhador ainda não pode se aposentar.")

if __name__ == "__main__":
    main()
