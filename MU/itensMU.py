lista_armas = []
lista_armaduras = []
lista_escudos = []
lista_pocoes = []
class Itens:
    def __init__(self, nome, raridade):
        self.nome = nome
        self.raridade = raridade


class Armas (Itens):
    def __init__(self, nome, raridade, dano):
        super().__init__(nome, raridade)
        self.dano = dano

    def equipar_Arma(self, personagem):
        personagem.ataque += self.dano 

    def __str__(self):
        return f"Arma: {self.nome}, Raridade: {self.raridade}, Dano: {self.dano}"

class Armaduras (Itens):
    def __init__(self, nome, raridade, defesa_eqp):
        super().__init__(nome, raridade)
        self.defesa_eqp = defesa_eqp

    def equipar_Defesa(self, personagem):
        personagem.defesa += self.defesa_eqp

    def __str__(self):
        return f"Armadura: {self.nome}, Raridade: {self.raridade}, Defesa: {self.defesa_eqp}"


class Escudos (Itens):
    def __init__(self, nome, raridade, escudo):
        super().__init__(nome, raridade)
        self.escudo = escudo

    def equipar_Escudo(self, personagem):
        personagem.escudo += self.defesa

    def __str__(self):
        return f"Escudo: {self.nome}, Raridade: {self.raridade}, Defesa extra: {self.escudo}"


    

class Pocoes (Itens):
    def __init__(self, nome, raridade, recuperar):
        super().__init__(nome, raridade)
        self.recuperar = recuperar

    def usar_Pocao(self, personagem):
        personagem.vida += self.recuperar

    def __str__(self):
        return f"Poção: {self.nome}, Raridade: {self.raridade}, Recupera: {self.recuperar} de vida"

Espada1 = Armas('Espada','Rara', 10)
Espada2 = Armas('Espada','Comum', 5)
lista_armas.append(Espada1)
lista_armas.append(Espada2)
for i in lista_armas:
    print (i)

Armadura1 = Armaduras('Armadura', 'Rara', 10)
Armadura2 = Armaduras('Armadura', 'Comum', 5)
lista_armaduras.append(Armadura1)
lista_armaduras.append(Armadura2)
for i in lista_armaduras:
    print (i)

Escudo1 = Escudos('Escudo', 'Rara', 10)
Escudo2 = Escudos('Escudo', 'Comum', 5)
lista_escudos.append(Escudo1)
lista_escudos.append(Escudo2)
for i in lista_escudos:
    print (i)

Pocao1 = Pocoes('Poção', 'Comum', 5)
lista_pocoes.append(Pocao1)
for i in lista_pocoes:
    print (i)
