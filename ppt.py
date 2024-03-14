import os
import time
import random

pontosVoce = 0
pontosComp = 0
numJogada = [1, 2, 3]
nomeJogada = ["Papel", "Pedra", "Tesoura"]

def cabecalho():
    os.system("cls" if os.name == "nt" else "clear")
    print("==============================================")
    print("Bem-vindo(a) ao jogo \"Pedra, Papel ou Tesoura\"")
    print("==============================================")
    print("\n")

def placar():
    print("PLACAR:")
    print(f"Você: {pontosVoce}")
    print(f"Você: {pontosComp}")
    print("\n")

def opcoes():
    print("Opções: 1 - Papel | 2 - Pedra | 3 - Tesoura")

def jogada(opcaoVoce, opcaoComp):
    print("==================")
    print(f"Sua jogada: {opcaoVoce}")
    print(f"Jogada do computador: {opcaoComp}")
    # FAZER A CONTA - lembrar que pode ter empate
    # indicar quem venceu
    print("==================")

while True:
    cabecalho()
    placar()
    opcoes()
    try:
        lanceVoce = int(input("Escolha seu lance: "))
        lanceComp = random.randint(1,3)
        print(lanceComp)
        # CHAMAR FUNÇÃO JOGADA COM DOIS PARÂMETROS (jogadaVoce e jogadaComp)
        # ATUALIZAR PLACAR
        # CHAMAR MENU DE JOGAR NOVAMENTE - Sim ou Não
        # Se sair mostra o placar final
        print(lanceVoce)
        break
    except:
        print("Insira apenas o número da opção (1, 2 ou 3). Tente novamente.")
        print("Voltando ao menu inicial...")
        time.sleep(3)
        continue