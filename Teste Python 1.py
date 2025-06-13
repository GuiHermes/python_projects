# x = int(input("Digite o valor de x:"))
# y = int(input("Digite o valor de y:"))

# z = (x**2)+(y**2)/(x-y)**2

# print (z)
# salario = float(input("Digite o seu salario:"))
# salario_reajustado = salario * 1.35

# print(salario_reajustado)

def menuinicial():
    print("MENU INICIAL\n")
    print("BEM-VINDO AO SUPERMERCADO\n")
    print(f"Codigo do Produto: {produtos['Arroz'][2]}\n Arroz: {produtos['Arroz'][0]} Quantidade: {produtos['Arroz'][1]}")
    print(f"Codigo do Produto: {produtos['Feijão'][2]}\n Feijão: {produtos['Feijão'][0]} Quantidade: {produtos['Feijão'][1]}")
    print(f"Codigo do Produto: {produtos['Carne'][2]}\n Carne: {produtos['Carne'][0]} Quantidade: {produtos['Carne'][1]}")
    print(f"Codigo do Produto: {produtos['Alface'][2]}\n Alface: {produtos['Alface'][0]} Quantidade: {produtos['Alface'][1]}")
       
produtos = {"Arroz":[17.90,2,1],
            "Feijão":[12.50,8,2],
            "Carne":[23.90,3,3],
            "Alface":[3.40,5,4]} 
valor_parcial = 0
valor_final = 0

# O código acima define uma função para exibir o menu inicial de um supermercado,
# onde são listados os produtos disponíveis com seus preços e quantidades em estoque.
while True:
    menuinicial()
    cod_produto = int(input("Digite o codigo do produto:"))
    qtd_produto = int(input("Digite a quantidade:"))
    if cod_produto == 1:
        if produtos["Arroz"][1] >= qtd_produto:
            produtos["Arroz"][1] -= qtd_produto
            valor_parcial += produtos["Arroz"][0] * qtd_produto
            valor_final += valor_parcial
            print(f"Você comprou {qtd_produto}kg de Arroz. Total: R${produtos['Arroz'][0] * qtd_produto:.2f}")
        else:
            print(f"Desculpe, não temos {qtd_produto}kg de Arroz em estoque. Temos apenas {produtos['Arroz'][1]}kg disponíveis.")
    elif cod_produto == 2:
        if produtos["Feijão"][1] >= qtd_produto:
            produtos["Feijão"][1] -= qtd_produto
            valor_parcial += produtos["Feijão"][0] * qtd_produto
            valor_final += valor_parcial
            print(f"Você comprou {qtd_produto}kg de Feijão. Total: R${produtos['Feijão'][0] * qtd_produto:.2f}")
        else:
            print(f"Desculpe, não temos {qtd_produto}kg de Feijão em estoque. Temos apenas {produtos['Feijão'][1]}kg disponíveis.")
    elif cod_produto == 3:
        if produtos["Carne"][1] >= qtd_produto:
            produtos["Carne"][1] -= qtd_produto
            valor_parcial += produtos["Carne"][0] * qtd_produto
            valor_final += valor_parcial
            print(f"Você comprou {qtd_produto}kg de Carne. Total: R${produtos['Carne'][0] * qtd_produto:.2f}")
        else:
            print(f"Desculpe, não temos {qtd_produto}kg de Carne em estoque. Temos apenas {produtos['Carne'][1]}kg disponíveis.")
    elif cod_produto == 4:
        if produtos["Alface"][1] >= qtd_produto:
            produtos["Alface"][1] -= qtd_produto
            valor_parcial += produtos["Alface"][0] * qtd_produto
            valor_final += valor_parcial
            print(f"Você comprou {qtd_produto}kg de Alface. Total: R${produtos['Alface'][0] * qtd_produto:.2f}")
        else:
            print(f"Desculpe, não temos {qtd_produto}kg de Alface em estoque. Temos apenas {produtos['Alface'][1]}kg disponíveis.")
    else:
        print("Código inválido. Tente novamente.")
    continuar = input("Deseja continuar comprando? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por comprar conosco!")
        print(f"Valor total da compra: R${valor_final:.2f}")
        break
# O código acima implementa um menu de supermercado onde o usuário pode comprar produtos específicos.
# Ele verifica a disponibilidade do produto e atualiza o estoque após a compra.
# O usuário pode continuar comprando ou sair do programa.
# O código é simples e direto, permitindo uma interação fácil com o usuário.    
        
   