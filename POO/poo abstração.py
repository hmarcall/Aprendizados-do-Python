from abc import ABC, abstractmethod

class Heroi(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def poder(self):
        pass

class Flash(Heroi):
    def poder(self):
        print(f'{self.nome} tem o poder de velocidade')

class Batman(Heroi):
    def poder(self):
        print(f'{self.nome} tem o poder de dinheiro')

lista = [
    Flash("Flash"),
         Batman("Batman")
]  
for i in lista:
    i.poder()
        

