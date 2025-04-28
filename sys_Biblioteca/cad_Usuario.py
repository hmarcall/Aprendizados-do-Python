class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

usuarios = {}

def criar_usuario(id, nome, email):
    novo_usuario = Usuario(id, nome, email)
    usuarios[id] = novo_usuario
    print(f"Usuário {nome} adicionado ao sistema!")

def listar_usuarios():
    for usuario in usuarios.values():
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
