salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

limite_prestacao = 0.2 * salario

if prestacao > limite_prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
