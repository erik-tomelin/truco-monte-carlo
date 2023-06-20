from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
import random

def temVencedor():
    if jogador1.rodadas >= 12:
        return 1
    elif jogador2.rodadas >= 12:
        return 2
    else:
        return 0

def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    jogador3.resetar()
    jogador4.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)
    jogador3.criarMao(baralho)
    jogador4.criarMao(baralho)

def mainGame():
    vitorias_time1 = 0
    vitorias_time2 = 0
    vitorias_rodada_time1 = 0
    vitorias_rodada_time2 = 0

    quem_ganhou = 0
    numero_de_repeticoes = 10000

    partidas = []

    for _ in range(numero_de_repeticoes):
        rodada = []

        time_primeira_rodada = 0

        vitorias_rodada_time1 = 0
        vitorias_rodada_time2 = 0

        quem_ganhou = 0

        jogador1.rodadas = 0
        jogador2.rodadas = 0

        jogador1.pontos = 0
        jogador2.pontos = 0

        jogadores = []

        while quem_ganhou == 0:
            if jogador1.rodadas == 0 and jogador2.rodadas == 0:
                if jogador1.pontos == 0 and jogador2.pontos == 0:
                    jogadores = ["jogador1", "jogador2", "jogador3", "jogador4"]
                    sorteado = random.choice(jogadores)

                    if sorteado == "jogador1" or sorteado == "jogador3":
                        time_primeira_rodada = 1
                    elif sorteado == "jogador2" or sorteado == "jogador4":
                        time_primeira_rodada = 2

                    if sorteado == "jogador1":
                        jogador1.primeiro = True
                        jogador2.ultimo = True
                    elif sorteado == "jogador2":
                        jogador2.primeiro = True
                        jogador3.ultimo = True
                    elif sorteado == "jogador3":
                        jogador3.primeiro = True
                        jogador4.ultimo = True
                    else:
                        jogador4.primeiro = True
                        jogador1.ultimo = True
                        
                    rodada = []
                    
            if jogador1.primeiro:
                jogador2.primeiro = True
                jogador1.ultimo = True
            elif jogador2.primeiro:
                jogador3.primeiro = True
                jogador2.ultimo = True
            elif jogador3.primeiro:
                jogador4.primeiro = True
                jogador3.ultimo = True
            else:
                jogador1.primeiro = True
                jogador4.ultimo = True

            if jogador1.mostrarMao() == [] and jogador2.mostrarMao() == [] and jogador3.mostrarMao() == [] and jogador4.mostrarMao() == []:
                reiniciarJogo()

            if jogador1.primeiro == True:
                if (jogador1.mostrarMao()):
                    carta_escolhida = jogador1.melhorNumero(manilha) if jogador1.melhorNumero(manilha) else 0
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = jogador2.melhorNumero(manilha) if jogador2.melhorNumero(manilha) else 0
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = jogador3.melhorNumero(manilha) if jogador3.melhorNumero(manilha) else 0
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = jogador4.melhorNumero(manilha) if jogador4.melhorNumero(manilha) else 0
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))
            elif jogador2.primeiro == True:
                if (jogador2.mostrarMao()):
                    carta_escolhida = jogador2.melhorNumero(manilha) if jogador2.melhorNumero(manilha) else 0
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = jogador3.melhorNumero(manilha) if jogador3.melhorNumero(manilha) else 0
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = jogador4.melhorNumero(manilha) if jogador4.melhorNumero(manilha) else 0
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = jogador1.melhorNumero(manilha) if jogador1.melhorNumero(manilha) else 0
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))
            elif jogador3.primeiro == True:
                if (jogador3.mostrarMao()):
                    carta_escolhida = jogador3.melhorNumero(manilha) if jogador3.melhorNumero(manilha) else 0
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = jogador4.melhorNumero(manilha) if jogador4.melhorNumero(manilha) else 0
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = jogador1.melhorNumero(manilha) if jogador1.melhorNumero(manilha) else 0
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = jogador2.melhorNumero(manilha) if jogador2.melhorNumero(manilha) else 0
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))
            elif jogador4.primeiro == True:
                if (jogador4.mostrarMao()):
                    carta_escolhida = jogador4.melhorNumero(manilha) if jogador4.melhorNumero(manilha) else 0
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = jogador1.melhorNumero(manilha) if jogador1.melhorNumero(manilha) else 0
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = jogador2.melhorNumero(manilha) if jogador2.melhorNumero(manilha) else 0
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = jogador3.melhorNumero(manilha) if jogador3.melhorNumero(manilha) else 0
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))
            else:
                print("Erro")

            carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
            carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())
            carta3 = Carta(carta_jogador_03.retornarNumero(), carta_jogador_03.retornarNaipe())
            carta4 = Carta(carta_jogador_04.retornarNumero(), carta_jogador_04.retornarNaipe())

            ganhador = jogo.verificarGanhador(carta1, carta2, carta3, carta4, manilha)
            
            jogo.quemJogaPrimeiro(jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador)
            jogo.adicionarPonto(jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador)

            if jogador1.pontos == 2:
                jogador1.adicionarRodada()
                jogador3.adicionarRodada()
                
                vitorias_rodada_time1 += 1

                reiniciarJogo()
            elif jogador2.pontos == 2:
                jogador2.adicionarRodada()
                jogador4.adicionarRodada()
                
                vitorias_rodada_time2 += 1

                reiniciarJogo()

            if (temVencedor() != 0):
                quem_ganhou = temVencedor()

                if (quem_ganhou == 1):
                    vitorias_time1 += 1
                elif (quem_ganhou == 2):
                    vitorias_time2 += 1

        print(len(partidas))

        rodada = [time_primeira_rodada, vitorias_rodada_time1, vitorias_rodada_time2]
        partidas.append(rodada)

    print(str(partidas))
    print("\nTime 1 Vitórias por Jogo - " + str(vitorias_time1))
    print("Time 2 Vitórias por Jogo - " + str(vitorias_time2))

    if vitorias_time1 > 0 and vitorias_time2 > 0:
        print(f"\nTime1 = " + str((vitorias_time1 / numero_de_repeticoes) * 100) + "% | Time2 = " + str((vitorias_time2 / numero_de_repeticoes) * 100) + "%")
    elif vitorias_time1 > 0:
        print(f"\nTime1 = " + str((vitorias_time1 / numero_de_repeticoes) * 100) + "% | Time2 = 0%") 
    elif vitorias_time2 > 0:
        print(f"\nTime1 = 0% | Time2 = " + str((vitorias_time2 / numero_de_repeticoes) * 100) + "%")

    inicia_ganha_time1 = 0
    inicia_ganha_time2 = 0
    
    escura = 0

    ganhou_de_0_time1 = 0
    ganhou_de_0_time2 = 0

    for rodadas in partidas:
        if (rodadas[1] == 12 and rodadas[2] == 11) or (rodadas[1] == 11 and rodadas[2] == 12):
            escura += 1
    
        if rodadas[1] == 12 and rodadas[2] == 0:
            ganhou_de_0_time1 += 1
        elif rodadas[1] == 0 and rodadas[2] == 12:
            ganhou_de_0_time2 += 1

        if rodadas[0] == 1 and rodadas[1] == 12:
            inicia_ganha_time1 += 1
        elif rodadas[0] == 2 and rodadas[2] == 12:
            inicia_ganha_time2 += 1

    print("\nQual a probabilidade do time que inicia a partida ganhar?")
    print("Time 1 inciou e ganhou " + str(inicia_ganha_time1) + " partida(s) (" + str((inicia_ganha_time1 / len(partidas)) * 100) + "%)")
    print("Time 2 inciou e ganhou " + str(inicia_ganha_time2) + " partida(s) (" + str((inicia_ganha_time2 / len(partidas)) * 100) + "%)")

    print("\nQual a probabilidade de acontecer 11/11")
    print("Aconteceu 11/11 (Escura) " + str(escura) + " vezes, que representa " + str((escura / len(partidas)) * 100) + "% das partidas")

    print("\nQual a probabilidade de acontecer 12/0 ou 0/12")
    print("Time 1 ganhou sem perder nenhuma " + str(ganhou_de_0_time1) + " vezes (" + str((ganhou_de_0_time1 / len(partidas)) * 100) + "%)")
    print("Time 2 ganhou sem perder nenhuma " + str(ganhou_de_0_time2) + " vezes (" + str((ganhou_de_0_time2 / len(partidas)) * 100) + "%)")

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)

    carta1 = 0
    carta2 = 0
    carta3 = 0
    carta4 = 0
    ganhador = 0

    nome = "Erik"
    jogador1 = jogo.criarJogador(nome, baralho)

    nome = "Malko"
    jogador3 = jogo.criarJogador(nome, baralho)

    nome = "Gab"
    jogador2 = jogo.criarJogador(nome, baralho)

    nome = "GabLiz"
    jogador4 = jogo.criarJogador(nome, baralho)

    mainGame()
