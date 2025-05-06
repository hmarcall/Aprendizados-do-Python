from livro import Livro


catalogo = []

while True:
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Buscar Livro")
    print("4. Definir disponibilidade Livro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            novo_Livro = Livro(
                titulo=input("Título: "), 
                autor=input("Autor: "), 
                ano=input("Ano: ")
                )
            catalogo.append(novo_Livro)
            continuar_add = input(f'Livro "{novo_Livro.titulo}" adicionado com sucesso!\n Deseja adicionar mais livros?\n  Digite "s" para sim ou "n" para não: ')
            if continuar_add.lower() != "s":
                break

    elif opcao == "2":
        if not catalogo:
            print("Nenhum livro cadastrado.")
        else:
            print("Livros cadastrados:")
            for indice, livro in enumerate(catalogo):
                print(f'{indice}, {livro.titulo}, {livro.autor}, {livro.ano}')

    elif opcao == "3":
        digit_Titulo = input("Digite o título do livro que deseja buscar: ")
        for livro in catalogo:
            if livro.titulo.lower() == digit_Titulo.lower():
                print(f'Livro encontrado: {livro.titulo}, {livro.autor}, {livro.ano}')
                break
            else:
                print("Livro não encontrado.")

    elif opcao == "4":
        digit_Titulo = input("Digite o título do livro que deseja definir a disponibilidade: ")
        for livro in catalogo:
            if livro.titulo.lower() == digit_Titulo.lower():
                status = input("Digite o status (disponivel/indisponivel): ")
                livro.disponibilidade(status)
                print(f'Livro "{livro.titulo}" atualizado para "{livro.status}".')
                break
            else:
                print("Livro não encontrado.")

    elif opcao == "5":
        break

    else:
        print("Opção inválida! Tente novamente.")


    