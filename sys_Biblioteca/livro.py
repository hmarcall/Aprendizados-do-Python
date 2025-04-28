class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = None
        self.usuario = None

    def adicionar_usuario(self, usuario):
        self.usuario = usuario
        print(f"Usuário {usuario.nome} adicionado ao livro {self.titulo}")

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponibilidade: {self.status}")
        if self.usuario:
            print(f"Emprestado para: {self.usuario.nome}, Email: {self.usuario.email}")
        else:
            print("Livro disponível para empréstimo")

    def disponibilidade(self, status):
        self.status = status
        if status == "disponivel":
            self.disponibilidade = True
        else:
            self.disponibilidade = False

