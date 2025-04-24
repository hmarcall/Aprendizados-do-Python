class Aluno:
    escola = "Escola Python"

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_dados(self):
        print(f'Nome: {self.nome}, Nota: {self.nota}, Escola: {Aluno.escola}')

digit1 = Aluno('Henrique', 10)
digit1.mostrar_dados()

