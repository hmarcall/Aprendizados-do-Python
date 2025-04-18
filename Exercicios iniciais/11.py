lista=[]
while True:
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Ver lista')
    print('0 - Sair do programa')

    opcao = str(input('Escolha uma opção:'))
    if opcao=='1':
        nome_Produto=input('Digite o nome do produto:')
        lista.append(nome_Produto)
        print(({nome_Produto}, 'foi adicionado à lista'))
    elif opcao=='2':
        lista.clear()
        print('Não há nada na lista')
    elif opcao=='3':
        print(lista)
    elif opcao=='0':
        print('Voce saiu do programa')
        break
    else:
        print('Opção invalida, tente novamente')


