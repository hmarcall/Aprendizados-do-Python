class Aluno:
    
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            print('APROVADO')
        else:
            print('REPROVADO')   

    def apresentar(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nNotas: {self.notas}\nMédia: {self.calcular_media():.2f}')

n_Henry = [10, 9, 10]
aluno1= Aluno('Henrique', 19, n_Henry)
aluno1.apresentar()
