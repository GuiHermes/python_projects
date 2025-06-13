import fpdf

pdf = fpdf.FPDF()
funcionarios = [
    {"Nome": "Thallita", "Idade": "25", "Cargo": "Analista", "ID": 1},
    {"Nome": "Guilherme", "Idade": "22", "Cargo": "Gerente", "ID": 2}
]

def gerar_pdf():
    if not funcionarios:
        print("Nenhum funcionário cadastrado para gerar o PDF.")
        return
    else:
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Relatório de Funcionários", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        for i, funcionario in enumerate(funcionarios, start=1):
            texto = f"{i}. Nome: {funcionario['Nome']}, Idade: {funcionario['Idade']}, Cargo: {funcionario['Cargo']}, ID: {funcionario['ID']}"
            pdf.cell(200, 10, txt=texto, ln=True)
        pdf.output("Funcionarios.pdf")
        print("=== PDF GERADO COM SUCESSO ===")
        
def cadastro_funcionario():
    print("=== Cadastro de Funcionarios ===")
    id_usuario = int(input("Digite o ID: "))
    if any(funcionario["ID"] == id_usuario for funcionario in funcionarios):
        print("Usuario já existe!")
        print("=== Voltando ao menu ===")
    else:        
        nome = input("Digite o nome do funcionario: ")
        idade = input(f"Digite a idade do(a) {nome}: ")
        cargo = input(f"Digite o cargo do(a) {nome}: ")
        funcionario = {"Nome":nome,"Idade":idade,"Cargo":cargo, "ID":id_usuario}
        funcionarios.append(funcionario)
        print(50*"=")
    
def listar_funcionario():
    print("=== Lista de Funcionarios ===")
    if not funcionarios:
        print("Nenhum funcionario cadastrado!")
    else:
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {funcionario['Nome']} Idade: {funcionario['Idade']} Cargo: {funcionario['Cargo']} ID: {funcionario['ID']}")
        
def menu():
    while True:
        print(50*"=")
        print("1 - Cadastro de funcionarios: ")
        print("2 - Lista de funcionarios: ")
        print("3 - Sair do cadastro: ")
        print("4 - Gerar PDF: ")
        print(50*"=")
        opcao = input("Qual a opção desejada? ")
        if opcao == "1":
            cadastro_funcionario()
        elif opcao == "2":
            listar_funcionario()
        elif opcao == "3":
            print(50*"=")
            print("Saindo do cadastro!")
            print(50*"=")        
            break
        elif opcao == "4":
            gerar_pdf()
        else:
            print("Opcão invalida, selecione uma opção de 1 a 3")
menu()
        
    