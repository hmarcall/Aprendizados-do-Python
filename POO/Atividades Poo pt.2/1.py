class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self):
            self.velocidade += 10
            
    def frear(self):
            if self.velocidade > 0:
                  self.velocidade -= 10
            else:
                  print ('Não foi possivel frear pois o carro ja está parado')

    def mostrar_dados(self):
        print(f'marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}, velocidade:{self.velocidade}')

carro1 = Carro('Volkwagem', 'Gol', 1998, 0)
carro1.mostrar_dados()
carro1.acelerar()
carro1.mostrar_dados()
carro1.frear()
carro1.mostrar_dados()


