from abc import ABC, abstractmethod
class Roupa(ABC):
        
    @abstractmethod
    def material(self):
        pass

class Camisa(Roupa):
    def material(self):
        print('Algodão')

class Calça(Roupa):
    def material(self):
        print('Jeans')

roupa1 = Camisa()
roupa2 = Calça()
roupa1.material()
roupa2.material()


