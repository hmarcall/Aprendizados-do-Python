from conn_estoque import PooDB

class Produto:
    def __init__(self, nome_produto, quantidade, categoria, descricao):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.categoria = categoria
        self.descricao = descricao

    def inserir(self, banco):
        banco.cursor.execute("INSERT INTO produto (nome_produto, quantidade, categoria, descricao) VALUES (?, ?, ?, ?)", (self.nome_produto, self.quantidade, self.categoria, self.descricao))
        banco.conn.commit()

def criar_produto():
    print("\n=== Cadastro de Novo Produto ===")
    nome_produto = input("Digite o nome: ")
    quantidade = int(input("Digite a quantidade: "))
    categoria = input("Digite o categoria: ")
    descricao = input("Digite a descricao: ")
    
    return Produto(nome_produto, quantidade, categoria, descricao)

def exibicao (banco):
    banco.cursor.execute('SELECT nome_produto FROM produto')
    return banco.cursor.fetchall()

def deletar(banco, nome_produto):
    banco.cursor.execute('DELETE FROM produto WHERE nome_produto = ?', (nome_produto,))
    banco.conn.commit()

def deletar(banco):
    banco.cursor.execute(UPDATE )
    dado = input("digite o dado a ser mudado"
                 conn.execute)

banco = PooDB()

while True:
    print("\n1 - Cadastrar novo produto")
    print('2 - Exibir produtos cadastrados')
    print('3 - Deletar um produto')
    print('4 - Atualizar um produto')
    print("5 - Sair")
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        novo_produto = criar_produto()
        novo_produto.inserir(banco)
        print("Produto cadastrado com sucesso!")

    elif opcao =='2':
        R_produtos = exibicao(banco)
        if R_produtos:
            print('Produtos cadastrados: ')
            for i in R_produtos:
                print(i[0])

    elif opcao == "3":
        D_produtos = input('Digite o nome do usuario que deseja excluir: ')
        produtos_cadastrados = [u[0] for u in exibicao(banco)]
        if D_produtos not in produtos_cadastrados:
            print ('Produto não encontrado no estoque')
        else:
            deletar(banco, D_produtos)
            print(f'\n{D_produtos} foi excluido de nossa base de dados')           

    elif opcao == "4":
        digit = input ('Deseja atualizar qual dado do estoque?\n')
        print ('1 - Nome do produto')
        print ('2 - Quantidade')
        print ('3 - Categoria')
        print ('4 - Descrição')
        
        if digit == '1':
            digit2 = input('Qual o nome do produto vc deseja atualizar?')



    elif opcao == "5":
        print("Saindo do programa...\n")
        banco.encerrar()
        break

    else:
        print("Opção inválida!")