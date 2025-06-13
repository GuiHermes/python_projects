from random import Random
import fpdf
from collections import Counter

aleatorizador = Random()
opcao = aleatorizador.randint(1,2)
gerador = 0
def menu():
    jogos= ["GTA", "MINECRAFT","CS" ]
    ganhador = []
    while True:
        print(10*"===")
        print("=== MENU ===")
        print("1 - Aleatorizar jogos:  ")
        # print("2 - Alterar numero de jogos: ")
        print("2 - Adicionar Jogo:" )
        print("3 - Listar Jogos")
        print("4 - Remover Jogo: ")
        print("5 - Sorteio seguidos:  ")
        print("6 - Sair")
        print(10*"===")
        
    
        opcao = int(input("Qual a opçao desejada: "))
        if opcao == 1:
            if not jogos:
                print("Não tem jogos para aleatorizar!")
            else:      
                gerador = int(aleatorizador.randint(0,len(jogos)-1))
                print(f"O jogo aleatorio escolhido foi: {jogos[gerador]}")
        # elif opcao == 2:
        #     y = 0
        #     y = int(input(f"Digite o numero de jogos: o valor não pode ser menor que {y} digite um numero a menos que a quantidade de jogos: "))  
        #     i = len(jogos)
        #     if y < i:
        #         print(f"O valor é menor que o numero de jogos! O numero de jogos é {i}!")
        elif opcao == 2:
            print(10*"===")
            novo_jogo = str(input("Qual o jogo que você quer adicionar?: "))
            jogosupp = novo_jogo.upper()
            if jogosupp not in jogos:
                print(f"O jogo {jogosupp} foi adicionado a jogos.")
                jogos.append(jogosupp)
            else:
                print("Esse jogo já está na lista de jogos!")
        elif opcao == 3:
            if not jogos:
                print("Nenhum jogo adicionado!")
            else:
                print(10*"===")
                print("=== Lista de jogos ===")
                for num, jogo in enumerate(jogos, start = 0):
                    print(f"{num}:{jogo}")  
                print(10*"===")    
        elif opcao == 4:
            print("=== Deletar Jogo ===")
            for num, jogo in enumerate(jogos, start = 0):
                print(f"{num}:{jogo}")
            delete = int(input("Qual jogo você quer deletar?:"))
            del jogos[delete]
            print("Jogo deletado com sucesso.")
        elif opcao == 5:
            print("=== Sorteador de Jogos ULTRA POWER ===")
            if not jogos:
                print("Nenhum jogo na lista!")
            else:    
                p = 0
                num_sorteio = int(input("Digite o numero de sorteios que você deseja: "))
                while p<num_sorteio:
                    gerador = aleatorizador.randint(0, len(jogos) - 1)
                    print(f"{p+1}º sorteio: {jogos[gerador]}")
                    ganhador.append(jogos[gerador])
                    contagem = Counter(ganhador)
                    p+=1  
                print("=== Jogos mais sorteados ===")
                for jogo, quantidade in contagem.most_common():
                    print(f"{jogo}: {quantidade} vezes")      
        elif opcao == 6:
            print("=== Saindo ===")
            break
        else:
            print("Opção invalida!")
            
menu()

        