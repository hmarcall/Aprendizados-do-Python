class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        print(f'Título: {self.titulo}, Autor {self.autor}, Ano: {self.ano}')

digit1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
digit1.descricao()

digit_Titulo = input('Digite o título do livro: ')
digit_Autor = input('Digite o autor do livro: ')
digit_Ano = int(input('Digite o ano do livro: '))

livro1=Livro(digit_Titulo, digit_Autor, digit_Ano)
livro1.descricao()