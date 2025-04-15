login = []
senha = []
D_login_C=(str(input('Crie um UserName:')))
login.append(D_login_C)
D_senha_C=(str(input('Crie uma Senha:')))
senha.append(D_senha_C)
print(login)
print(senha)
print ('Seu cadastro foi realizado com sucesso!')
D_login=(str(input('Digite seu UserName:')))
D_senha=(str(input('Digite sua Senha:')))
while D_login[0] != login[0] and D_senha[0] != senha[0]:
    print('Login ou senha incorretos, tente novamente')
    D_login=(str(input('Digite seu UserName:')))
    D_senha=(str(input('Digite sua Senha:')))
    if D_login in login and D_senha in senha:
        print('Login realizado com sucesso')
        break

compras = []

while True:
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Ver posição de um item")
    print("5 - Contar quantas vezes um item aparece")
    print("6 - Limpar lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in compras:
            compras.remove(item)
            print(f'"{item}" foi removido.')
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        print("\nSua lista de compras:")
        print(compras)

    elif opcao == "4":
        item = input("Digite o nome do item: ")
        if item in compras:
            print(f"O item '{item}' está na posição {compras.index(item)}.")
        else:
            print("Item não encontrado.")

    elif opcao == "5":
        item = input("Digite o item para contar: ")
        qtd = compras.count(item)
        print(f"O item '{item}' aparece {qtd} vezes na lista.")

    elif opcao == "6":
        compras.clear()
        print("Lista de compras esvaziada!")

    elif opcao == "0":
        print("Saindo... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
