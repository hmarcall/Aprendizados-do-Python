dicio = {
    'Refrigerantes e sucos' : {},
    'Bebidas alcolicas' : {}
    }
opcao = 0
while True:
    print("1. Refrigerantes e sucos")
    print("2. Bebidas alcolicas")
    print("0. Sair")
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        while True:
            dicio['Refrigerantes e sucos'] = input('Digite refrigerantes ou sucos para adicionar: ')
            print(dicio['Refrigerantes e sucos'])
            if input('Selecione uma opção: ') == "sair":
                break
    elif opcao == 2:
        while True:
            dicio['Bebidas alcolicas'] = input('Digite bebidas alcolicas para adicionar: ')
            print(dicio['Bebidas alcolicas'])
            if input('Selecione uma opção: ') == "sair":
                break
    elif opcao == 0:
        break

    
        
