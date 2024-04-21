def calcular_media_ponderada(nota1, nota2):
    peso_prova1 = 1
    peso_prova2 = 2
    
    media_ponderada = (nota1 * peso_prova1 + nota2 * peso_prova2) / (peso_prova1 + peso_prova2)
    
    return media_ponderada

def verificar_aprovacao(media):
    nota_aprovacao = 70
    
    if media >= nota_aprovacao:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    
    media = calcular_media_ponderada(nota1, nota2)
    
    resultado = verificar_aprovacao(media)
    
    print("Média do aluno:", media)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
