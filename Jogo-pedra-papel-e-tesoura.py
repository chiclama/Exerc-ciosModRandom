from random import choice

Jogador_vitorias = 0
maq_vitorias = 0

def opção_jogador():
    escolha_jogador = input("escolhe Pedra, Papel ou Tesoura: ")
    escolha_jogador.lower()
    if escolha_jogador == "pedra":
        return escolha_jogador
    elif escolha_jogador == "papel":
        return escolha_jogador 
    elif escolha_jogador == "tesoura":
        return escolha_jogador
    else:
        print("Opção invalida, tente de novo ")
        opção_jogador()

def opção_maquina():
    escolha_maquina = choice(["pedra","papel","tesoura"])
    return escolha_maquina 


while True:

    print("-"*30)
    escolha_jogador = opção_jogador()
    escolha_maquina = opção_maquina()
    print("-"*30)

    if(escolha_jogador == "pedra") and (escolha_maquina == "tesoura") \
        or (escolha_jogador == "papel") and (escolha_maquina== "pedra") \
           or (escolha_jogador == "tesoura") and (escolha_maquina == "papel"):
           print(f"jogador escolheu {escolha_jogador} e a máquina escolheu {escolha_maquina}"
           ",resultado: Você ganhoooou desgraaaaça!!!!")
           Jogador_vitorias += 1
    elif escolha_jogador == escolha_maquina:
        print(f"jogador escolheu {escolha_jogador} e a máquina escolheu {escolha_maquina}"
        " Resultado: DEEEEU EMPAAATE!!!")
    else:
        print(f"jogador escolheu {escolha_jogador} e a máquina escolheu {escolha_maquina}"
        " Resultado: você perdeu")
        maq_vitorias += 1

    
    print("-"*30)
    print(f"vitórias do jogador: {Jogador_vitorias}")
    print(f"Vitórias da máquina: {maq_vitorias}")
    print("-"*30)

    jogador_escolhe = input("Opa, bora mais uma partidinha? ")
    if jogador_escolhe in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif jogador_escolhe in ["NAO","nao", "Nao", "n", "N","NÃO"]:
        break
    else:
        break

