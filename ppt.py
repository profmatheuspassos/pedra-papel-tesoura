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
    print(f"Computador: {pontosComp}")
    print("\n")

def placarFinal():
    print("PLACAR FINAL:")
    print(f"Você: {pontosVoce}")
    print(f"Computador: {pontosComp}\n")
    if pontosComp > pontosVoce:
        print("O computador venceu!")
    elif pontosComp < pontosVoce:
        print("Você venceu!")
    else:
        print("Deu empate!")
    print("\n")
    print("Até a próxima!")
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

def erroOpcoes():
    print("Insira apenas o número 1 ou o número 2.")
    print("Voltando ao menu inicial...")
    time.sleep(3)

def opcoes():
    print("Opções: 1 - Papel | 2 - Pedra | 3 - Tesoura")

def jogada(opcaoVoce, opcaoComp):
    global pontosVoce, pontosComp
    print("==================")
    print(f"Sua jogada: {opcaoVoce}")
    print(f"Jogada do computador: {opcaoComp}")
    if opcaoVoce > opcaoComp:
        print("Você venceu!")
        pontosVoce += 1
    elif opcaoVoce < opcaoComp:
        print("O computador venceu!")
        pontosComp += 1
    else:
        print("Empate!")
        pontosComp += 1
        pontosVoce += 1
    print("Pontuação atual:")
    print(f"Você: {pontosVoce} - Computador: {pontosComp}")
    print("==================")

while True:
    cabecalho()
    placar()
    opcoes()
    try:
        lanceVoce = int(input("\nEscolha seu lance: "))
        lanceComp = random.randint(1,3)
        jogada(lanceVoce, lanceComp)
        try:
            sair = int(input("Você quer sair ou jogar novamente? 1 - SAIR | 2 - JOGAR NOVAMENTE"))
            if sair == 1:
                placarFinal()
                break
            elif sair == 2:
                print("Voltando ao menu inicial...")
                time.sleep(3)
                continue
            else:
                erroOpcoes()
                continue
        except:
            erroOpcoes()
            continue
        # CHAMAR FUNÇÃO JOGADA COM DOIS PARÂMETROS (jogadaVoce e jogadaComp)
        # ATUALIZAR PLACAR
        # CHAMAR MENU DE JOGAR NOVAMENTE - Sim ou Não
        # Se sair mostra o placar final
        break
    except:
        print("Insira apenas o número da opção (1, 2 ou 3). Tente novamente.")
        print("Voltando ao menu inicial...")
        time.sleep(3)
        continue