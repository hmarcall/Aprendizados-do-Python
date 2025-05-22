from Conn import PooDB

class Usuario:
    def __init__(self, nome, idade, sobrenome, cidade):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        self.cidade = cidade

    def inserir(self, banco):
        banco.cursor.execute("INSERT INTO usuario (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)", (self.nome, self.idade, self.sobrenome, self.cidade))
        banco.conn.commit()

def criar_usuario():
    print("\n=== Cadastro de Novo Usuário ===")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sobrenome = input("Digite o sobrenome: ")
    cidade = input("Digite a cidade: ")
    
    return Usuario(nome, idade, sobrenome, cidade)

# Código principal
if __name__ == "__main__":
    banco = PooDB()
    
    while True:
        print("\n1 - Cadastrar novo usuário")
        print("2 - Sair")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            novo_usuario = criar_usuario()
            novo_usuario.inserir(banco)
            print("Usuário cadastrado com sucesso!")
        elif opcao == "2":
            print("\nUsuario(s) cadastrado(s) com sucesso!\n")
            print("Saindo do programa...")
            banco.encerrar
            break
        else:
            print("Opção inválida!")

