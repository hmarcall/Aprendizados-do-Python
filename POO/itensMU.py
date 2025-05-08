lista_armas = []
class Itens:
    def __init__(self, nome, raridade):
        self.nome = nome
        self.raridade = raridade

class Armas(Itens):
    def __init__(self, nome, raridade, dano):
        super().__init__(nome, raridade)
        self.dano = dano

    def equipar_Arma(self):
        self.ataque += self.dano 

class Armaduras (Itens):
    def __init__(self, nome, raridade, defesa_eqp):
        super().__init__(nome, raridade)
        self.defesa_eqp = defesa_eqp

    def equipar_Defesa(self):
        self.defesa += self.defesa_eqp


class Escudos (Itens):
    def __init__(self, nome, raridade, escudo):
        super().__init__(nome, raridade)
        self.escudo = escudo

    def equipar_Escudo(self):
        self.escudo += self.defesa

class Pocoes (Itens):
    def __init__(self, nome, raridade, recuperar):
        super().__init__(nome, raridade)
        self.recuperar = recuperar

    def usar_Pocao(self):
        self.vida += self.recuperar
Espada1 = Armas('Espada de Fogo', 'Rara', 10)
Espada2 = Armas('Espada de Gelo', 'Comum', 5)
lista_armas.append(Espada1)
lista_armas.append(Espada2)
for i in lista_armas:
    print (i)
