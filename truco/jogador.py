class Jogador():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.pontos = 0
        self.rodadas = 0
        self.primeiro = False
        self.ultimo = False
    
    def criarMao(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
    
    def jogarCarta(self, carta_escolhida):
        return self.mao.pop(carta_escolhida)
    
    def mostrarMao(self):
        listaMao = []

        for carta in self.mao:
            if carta.numero == 1:
                listaMao.append(f"A de {carta.naipe}")
            elif carta.numero == 13:
                listaMao.append(f"K de {carta.naipe}")
            elif carta.numero == 12:
                listaMao.append(f"Q de {carta.naipe}")
            elif carta.numero == 11:
                listaMao.append(f"J de {carta.naipe}")
            else:
                listaMao.append(f"{carta.numero} de {carta.naipe}")
            
        return listaMao
    
    def adicionarPonto(self):
        self.pontos += 1
    
    def adicionarRodada(self):
        self.rodadas +=1
    
    def resetar(self):
        self.pontos = 0
        self.mao = []
    
    def melhorNumero(self, manilha):
       for carta in self.mao:
            if (manilha == carta.numero):
                if carta.numero == 1:
                    return f"A de {carta.naipe}"
                elif carta.numero == 13:
                    return f"K de {carta.naipe}"
                elif carta.numero == 12:
                    return f"Q de {carta.naipe}"
                elif carta.numero == 11:
                    return f"J de {carta.naipe}"
                else:
                    return f"{carta.numero} de {carta.naipe}"

            if carta.numero == 3:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 2:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 1:
                return f"A de {carta.naipe}"
            elif carta.numero == 13:
                return f"K de {carta.naipe}"
            elif carta.numero == 12:
                return f"Q de {carta.naipe}"
            elif carta.numero == 11:
                return f"J de {carta.naipe}"
            elif carta.numero == 10:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 9:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 8:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 7:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 6:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 5:
                return f"{carta.numero} de {carta.naipe}"
            elif carta.numero == 4:
                return f"{carta.numero} de {carta.naipe}"
            else:
                return False
