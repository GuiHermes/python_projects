print(100*"=")
nome_funcionario = input("Digite o nome do funcionario:")
nome_funcionario_title = nome_funcionario.title()
cargo_funcionario = input("Digite o cargo do funcionario:(Gerente, Auxiliar, Produção)")
cargo_funcionario_lower = cargo_funcionario.lower()
cargo_funcionario_title = cargo_funcionario.title()
print(100*"=")
salario_funcionario = 0.0
if cargo_funcionario_lower == "gerente":
    salario_funcionario = 5600.00
    print(f"Cadastro do funcionario: {nome_funcionario_title} concluido.\nSalario inicial: {salario_funcionario}\nCargo: {cargo_funcionario_title}")
elif cargo_funcionario_lower == "auxiliar":
    salario_funcionario = 2100.00
    print(f"Cadastro do funcionario: {nome_funcionario_title} concluido.\nSalario inicial: {salario_funcionario}\nCargo: {cargo_funcionario_title}")
elif cargo_funcionario_lower == "producao":
    salario_funcionario = 1600.00
    print(f"Cadastro do funcionario: {nome_funcionario_title} concluido.\nSalario inicial: {salario_funcionario}\nCargo: {cargo_funcionario_title}")
else:
    print(f"Cadastro invalido, cargo {cargo_funcionario} não existe!")
continuar = input("Deseja continuar?(Sim/Nao)")
continuar_lower = continuar.lower()
if continuar_lower == "sim":
    reajustar = input(f"Deseja aplicar o reajuste salarial para o funcionario {nome_funcionario_title} {cargo_funcionario_title}?")
    reajustar = reajustar.lower()
    if reajustar == "sim":
        novo_salario = salario_funcionario*1.15
        print(100*"=")
        print("Os dados do funcionario são:")
        print(f"Nome: {nome_funcionario_title}\nCargo: {cargo_funcionario_title}\nSalario: {novo_salario:.2f}")
        print(100*"=")
    else:
        print("Não houve reajuste.")
else:
    print(100*"=")
    print("Os dados do funcionario são:")
    print(f"Nome: {nome_funcionario_title}\nCargo: {cargo_funcionario_title}\nSalario: {salario_funcionario:.2f}")
    print(100*"=")
        


    