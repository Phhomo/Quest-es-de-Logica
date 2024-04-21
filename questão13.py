def calcular_media_final(nota_lab, nota_semestral, nota_final):
    peso_lab = 2
    peso_semestral = 3
    peso_final = 5
    
    media_final = (nota_lab * peso_lab + nota_semestral * peso_semestral + nota_final * peso_final) / (peso_lab + peso_semestral + peso_final)
    
    return media_final

def verificar_situacao(media_final):
    if media_final < 3.0:
        return "Reprovado"
    elif media_final < 5.0:
        return "Em recuperação"
    else:
        return "Aprovado"

def main():
    nota_lab = float(input("Digite a nota do trabalho de laboratório: "))
    nota_semestral = float(input("Digite a nota da avaliação semestral: "))
    nota_final = float(input("Digite a nota do exame final: "))
    
    media_final = calcular_media_final(nota_lab, nota_semestral, nota_final)
    
    situacao = verificar_situacao(media_final)
    
    print("Média final do aluno:", media_final)
    print("Situação do aluno:", situacao)

if __name__ == "__main__":
    main()
