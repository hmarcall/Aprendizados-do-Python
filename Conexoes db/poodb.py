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

def exibicao (banco):
    banco.cursor.execute('SELECT nome FROM usuario')
    return banco.cursor.fetchall()

def deletar(banco, nome):
    banco.cursor.execute('DELETE FROM usuario WHERE nome = ?', (nome,))
    banco.conn.commit()

banco = PooDB()

while True:
    print("\n1 - Cadastrar novo usuário")
    print('2 - Exibir cadastrados')
    print('3 - Deletar um usuario')
    print("4 - Sair")
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        novo_usuario = criar_usuario()
        novo_usuario.inserir(banco)
        print("Usuário cadastrado com sucesso!")

    elif opcao =='2':
        R_usuarios = exibicao(banco)
        if R_usuarios:
            print('Usuarios cadastrados: ')
            for i in R_usuarios:
                print(i[0])

    elif opcao == "3":
        D_usuarios = input('Digite o nome do usuario que deseja excluir: ')
        usuarios_cadastrados = [u[0] for u in exibicao(banco)]
        if D_usuarios not in usuarios_cadastrados:
            print ('Usuario não encontrado em nossa base de dados')
        else:
            deletar(banco, D_usuarios)
            print(f'\n{D_usuarios} foi excluido de nossa base de dados')    
        

    elif opcao == "4":
        print("Saindo do programa...\n")
        banco.encerrar()
        break
    else:
        print("Opção inválida!")


