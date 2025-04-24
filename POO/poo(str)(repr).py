class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    def __str__(self):
        return f"Filme: {self.titulo} ({self.ano}) - {self.genero}"

    def __repr__(self):
        return f"Filme('{self.titulo}', {self.ano}, '{self.genero}')"

# Testando:
f1 = Filme("Matrix", 1999, "Ficção Científica")

print(f1)   # Usa __str__: Filme: Matrix (1999) - Ficção Científica
f1         # Usa __repr__: Filme('Matrix', 1999, 'Ficção Científica')
