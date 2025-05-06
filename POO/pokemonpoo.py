class Pokemon:
    def __init__(self, nome, tipo, poderes):
        self.nome = nome
        self.tipo = tipo
        self.poderes = poderes

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}, Tipo: {self.tipo}, Poderes: {self.poderes}')

p1 = Pokemon('Arthur', 'Preto', 'Desaparece em meio à escuridao da noite')
p2 = Pokemon('Kayk', 'Preto', 'Camufla no escuro')
p1.exibir_informacoes()
p2.exibir_informacoes()