# Função para exibir o menu de opções
def exibir_menu():
    print("\nCalculadora Simples")
    print("Escolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

# Função principal da calculadora
def calculadora():
    while True:
        exibir_menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Saindo da calculadora. Até logo!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif escolha == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif escolha == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif escolha == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Por favor, digite valores numéricos válidos.")
        else:
            print("Opção inválida. Tente novamente.")

# Executa a calculadora
calculadora()
