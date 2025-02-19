from random import choice

print("-"*30)
print("-"*30)
print("BEM VINDO AO TIGRINHO DO CADU")
print("-"*30)
dinheiro = 100
print("-"*30)
print(f"Você tem {dinheiro} de saldo")
print("-"*30)
perda = 20
ganho = 100000
def jogoDoTiger(Entra,Ganho,perda):#Entra == o valor inicial/Ganho == ganho/ perda == perda
    lista = ["ouro", "prata", "ouro"]
    while True:
        escolha1 = choice(lista)
        escolha2 = choice(lista)
        escolha3 = choice(lista)
        Jogador_escolhe = input("clique G e de ENTER para girar a maquina ")
        if Jogador_escolhe in ["G", "g"]:
            print("-"*30)
            print(f"a primeira maquina girou o {escolha1}")
            print("-"*30)
            print(f"a segunda maquina girou o {escolha2}")
            print("-"*30)
            print(f"a terceira maquina girou o {escolha3}")
            print("-"*30)
            pass
        if escolha1 == escolha2 == escolha3:
            print("PARABÉNS VOCÊ GANHOU" )
            Entra += Ganho  
            print(F"VOCÊ TEM {Entra} de saldo")
            repetição = input("quer ir mais uma? ")
            if repetição in ["sim", "Sim", "SIM"]:
                print(f"O seu saldo é de {Entra}")
            elif repetição in ["não", "nao", "Nao", "NAO"]:
                break
            else:
                break
        else:
            Entra -= perda
            print(f"O seu saldo é de {Entra}")
            repetição = input("Opa, você perdeu mas agora você vai ganhar eu acredito, bora mais uma? ")
            if repetição in ["sim", "Sim", "SIM"]:
                print(f"O seu saldo é de {Entra}")
            elif repetição in ["não", "nao", "Nao", "NAO"]:
                break
            else:
                 break

iniciativa = input("Bora jogar um tigrinho?? ")

if iniciativa in ["sim", "SIM", "Sim"]:
    jogoDoTiger(dinheiro,ganho,perda)
    print(f"dinheiro restante: {dinheiro}")




