from random import Random
import fpdf
jogos= ["GTA", "MINECRAFT","CS" ]
aleatorizador = Random()
opcao = aleatorizador.randint(1,2)
gerador = 0

def aleatorizar(): 
    if not jogos:
         print("Não tem jogos para aleatorizar!")
    else:      
        gerador = int(aleatorizador.randint(0,len(jogos)-1))
        print(f"O jogo aleatorio escolhido foi: {jogos[gerador]}")
        
def adicionar_jogos():
    print(10*"===")
    novo_jogo = str(input("Qual o jogo que você quer adicionar?: "))
    if novo_jogo not in jogos:
        print(f"O jogo {novo_jogo} foi adicionado a jogos.")
        jogosupp = novo_jogo.upper()
        jogos.append(jogosupp)
    else:
        print("Esse jogo já está na lista de jogos!")

def listar_jogos():
    if not jogos:
        print("Nenhum jogo adicionado!")
    else:
        print(10*"===")
        print("=== Lista de jogos ===")
        for num, jogo in enumerate(jogos, start = 0):
            print(f"{num}:{jogo}")  
        print(10*"===")

def remover_jogos():
    for num, jogo in enumerate(jogos, start = 0):
        print(f"{num}:{jogo}")
        delete = int(input("Qual jogo você quer deletar?:"))
        del jogos[delete]
        print("Jogo deletado com sucesso.")
       
def sorteio_seg():
    if not jogos:
        print("Nenhum jogo na lista!")
    else:    
        p = 0
        num_sorteio = int(input("Digite o numero de sorteios que você deseja: "))
        while p<num_sorteio:
             gerador = aleatorizador.randint(0, len(jogos) - 1)
             print(f"{p+1}º sorteio: {jogos[gerador]}")
             p+=1

# def alterar_num_jogos():
#     y = 0
#     y = int(input(f"Digite o numero de jogos: o valor não pode ser menor que {y} digite um numero a menos que a quantidade de jogos: "))  
#     i = len(jogos)
#     if y < i:
#         print(f"O valor é menor que o numero de jogos! O numero de jogos é {i}!")
         

def menu():
    while True:
        print("======= MENU =======")
        print("1 - Aleatorizar jogos:  ")
        # print("2 - Alterar numero de jogos: ") opção que desativei por não fazer sentido
        print("2 - Adicionar Jogo:" )
        print("3 - Listar Jogos")
        print("4 - Remover Jogo: ")
        print("5 - Sorteio seguidos:  ")
        print("6 - Sair")
        print(10*"===")
        
        opcao = int(input("Qual a opçao desejada: "))
        if opcao == 1:
            aleatorizar()
        elif opcao == 2:
            adicionar_jogos()
        elif opcao == 3:
            listar_jogos()    
        elif opcao == 4:
            remover_jogos()
        elif opcao == 5:
            sorteio_seg()        
        elif opcao == 6:
            print("=== Saindo ===")
            break
        else:
            print("Opção invalida!")
            
menu()

        