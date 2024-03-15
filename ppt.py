import os
import time
import random

pontosVoce = 0
pontosComp = 0
nomesJogadas = {1: "Papel", 2: "Pedra", 3: "Tesoura"}

def cabecalho():
    os.system("cls" if os.name == "nt" else "clear")
    print("==============================================")
    print("Bem-vindo(a) ao jogo \"Pedra, Papel ou Tesoura\"")
    print("==============================================\n")

def placar():
    print("PLACAR:")
    print(f"Você: {pontosVoce}")
    print(f"Computador: {pontosComp}\n")

def placarFinal():
    cabecalho()
    print("PLACAR FINAL:")
    print(f"Você: {pontosVoce}")
    print(f"Computador: {pontosComp}\n")
    if pontosComp > pontosVoce:
        print("O computador venceu!")
    elif pontosComp < pontosVoce:
        print("Você venceu!")
    else:
        print("Deu empate!")
    print("\nAté a próxima!")
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

def erroOpcoes():
    print("Insira apenas o número 1, 2 ou 3.")
    print("Voltando ao menu inicial...")
    time.sleep(3)

def opcoes():
    print("Opções: 1 - Papel | 2 - Pedra | 3 - Tesoura")

def verificaVencedor(nomeJogadaVoce, nomeJogadaComp):
    if (nomeJogadaVoce == "Papel" and nomeJogadaComp == "Pedra") or \
       (nomeJogadaVoce == "Pedra" and nomeJogadaComp == "Tesoura") or \
       (nomeJogadaVoce == "Tesoura" and nomeJogadaComp == "Papel"):
        return "voce"
    elif nomeJogadaVoce == nomeJogadaComp:
        return "empate"
    else:
        return "comp"

def jogada(opcaoVoce, opcaoComp):
    global pontosVoce, pontosComp
    nomeJogadaVoce = nomesJogadas[opcaoVoce]
    nomeJogadaComp = nomesJogadas[opcaoComp]
    resultado = verificaVencedor(nomeJogadaVoce, nomeJogadaComp)
    print("==================")
    print(f"Sua jogada: {nomeJogadaVoce}")
    print(f"Jogada do computador: {nomeJogadaComp}")
    if resultado == "voce":
        print("Você venceu!")
        pontosVoce += 1
    elif resultado == "comp":
        print("O computador venceu!")
        pontosComp += 1
    else:
        print("Empate!")
    print(f"Pontuação atual: Você: {pontosVoce} - Computador: {pontosComp}")
    print("==================")

while True:
    cabecalho()
    placar()
    opcoes()
    try:
        lanceVoce = int(input("\nEscolha seu lance (1, 2 ou 3): "))
        if lanceVoce not in [1, 2, 3]:
            raise ValueError("Opção inválida.")
        lanceComp = random.randint(1,3)
        jogada(lanceVoce, lanceComp)

        sairOpcaoValida = False
        while not sairOpcaoValida:
            try:
                print("Você quer sair ou jogar novamente? 1 - SAIR | 2 - JOGAR NOVAMENTE")
                sair = int(input("Digite o número da sua opção: "))
                if sair == 1:
                    placarFinal()
                    break
                elif sair == 2:
                    print("Voltando ao menu inicial...")
                    time.sleep(3)
                    sairOpcaoValida = True
                else:
                    raise ValueError("Opção inválida.")
            except ValueError:
                erroOpcoes()
    except ValueError:
        print("Insira apenas o número da opção (1, 2 ou 3). Tente novamente.")
        time.sleep(3)
