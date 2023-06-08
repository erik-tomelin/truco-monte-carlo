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
    
    quem_ganhou = 0
    numero_de_repeticoes = 100

    for _ in range(numero_de_repeticoes):

        while quem_ganhou == 0:
            if jogador1.rodadas == 0 and jogador2.rodadas == 0:
                if jogador1.pontos == 0 and jogador2.pontos == 0:
                    jogadores = ["jogador1", "jogador2",
                                 "jogador3", "jogador4"]
                    sorteado = random.choice(jogadores)
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

            if jogador1.primeiro == True:
                if (jogador1.mostrarMao()):
                    carta_escolhida = random.choice(jogador1.mostrarMao()) if random.choice(jogador1.mostrarMao()) else 0
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = random.choice(jogador2.mostrarMao())
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = random.choice(jogador3.mostrarMao())
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = random.choice(jogador4.mostrarMao())
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))
            elif jogador2.primeiro == True:
                if (jogador2.mostrarMao()):
                    carta_escolhida = random.choice(jogador2.mostrarMao())
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = random.choice(jogador3.mostrarMao())
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = random.choice(jogador4.mostrarMao())
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = random.choice(jogador1.mostrarMao())
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))
            elif jogador3.primeiro == True:
                if (jogador3.mostrarMao()):
                    carta_escolhida = random.choice(jogador3.mostrarMao())
                    carta_jogador_03 = jogador3.jogarCarta(jogador3.mostrarMao().index(carta_escolhida))

                if (jogador4.mostrarMao()):
                    carta_escolhida = random.choice(jogador4.mostrarMao())
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = random.choice(jogador1.mostrarMao())
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = random.choice(jogador2.mostrarMao())
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))
            elif jogador4.primeiro == True:
                if (jogador4.mostrarMao()):
                    carta_escolhida = random.choice(jogador4.mostrarMao())
                    carta_jogador_04 = jogador4.jogarCarta(jogador4.mostrarMao().index(carta_escolhida))

                if (jogador1.mostrarMao()):
                    carta_escolhida = random.choice(jogador1.mostrarMao())
                    carta_jogador_01 = jogador1.jogarCarta(jogador1.mostrarMao().index(carta_escolhida))

                if (jogador2.mostrarMao()):
                    carta_escolhida = random.choice(jogador2.mostrarMao())
                    carta_jogador_02 = jogador2.jogarCarta(jogador2.mostrarMao().index(carta_escolhida))

                if (jogador3.mostrarMao()):
                    carta_escolhida = random.choice(jogador3.mostrarMao())
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
                # print(f"\n{jogador1.nome} e {jogador3.nome} ganharam a rodada")
                reiniciarJogo()

            elif jogador2.pontos == 2:
                jogador2.adicionarRodada()
                jogador4.adicionarRodada()
                # print(f"\n{jogador2.nome} e {jogador4.nome} ganharam a rodada")
                reiniciarJogo()

            jogo.quemIniciaRodada(jogador1, jogador2, jogador3, jogador4)

            if (temVencedor() != 0):
                quem_ganhou = temVencedor()

                if (quem_ganhou == 1):
                    vitorias_time1 += 1
                elif (quem_ganhou == 2):
                    vitorias_time2 += 1
        quem_ganhou = 0

    print("\ntime1 " + str(vitorias_time1))
    print("time2 " + str(vitorias_time2))
    if vitorias_time1 > 0 and vitorias_time2 > 0:
        print(f"\nTime1 = " + str((vitorias_time1 / numero_de_repeticoes) * 100) + "% | Time2 = " + str((vitorias_time2 / numero_de_repeticoes) * 100) + "%")
    elif vitorias_time1 > 0:
        print(f"\nTime1 = " + str((vitorias_time1 / numero_de_repeticoes) * 100) + "% | Time2 = 0%") 
    elif vitorias_time2 > 0:
        print(f"\nTime1 = 0% | Time2 = " + str((vitorias_time2 / numero_de_repeticoes) * 100) + "%")


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

    print("\nTime 1")
    nome = "Erik"
    jogador1 = jogo.criarJogador(nome, baralho)

    nome = "Malko"
    jogador3 = jogo.criarJogador(nome, baralho)

    print("Time 2")
    nome = "Gab Borowiak"
    jogador2 = jogo.criarJogador(nome, baralho)

    nome = "Gab Liz"
    jogador4 = jogo.criarJogador(nome, baralho)

    mainGame()
