produtos=[]
while True:
    produto = {}
    produto['nome'] = input('Digite o nome do produto que deseja adicionar a seu carrinho: ')
    produto['preço'] = float(input('Digite o preço do produto: '))

    produtos.append(produto)
    
    parar = input('Deseja finalizar a compra?\n Para finalizar digite "s", para continuar adicionano produtos à seu carrinho digite "n": ')
    if parar.lower() == 's':
        break
for i in produtos:
    print(f'Produto: {i['nome']}, Preço: {i['preço']}')
total = sum([p['preço'] for p in produtos])
print(f"Total da compra: R$ {total:.2f}")

