numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    maior = numero1
    diferenca = numero1 - numero2
else:
    maior = numero2
    diferenca = numero2 - numero1

print("O maior número é:", maior)
print("A diferença entre os números é:", diferenca)
