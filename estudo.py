
funcionarios = []

def cadastrar_funcionario():
    print("\n--- Cadastro de Funcionário ---")
    nome = input("Digite o nome do funcionário: ")
    idade = input("Digite a idade do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    funcionario = {"Nome": nome, "Idade": idade, "Cargo": cargo}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!\n")

def listar_funcionarios():
    print("\n--- Lista de Funcionários ---")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
    else:
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {funcionario['Nome']}, Idade: {funcionario['Idade']}, Cargo: {funcionario['Cargo']}")
        print()

def menu():
    while True:
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
menu()
