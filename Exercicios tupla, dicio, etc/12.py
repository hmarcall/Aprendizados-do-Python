pessoas = []  
for i in range(5):
    pessoa = {}
    pessoa['nome'] = input('Digite seu nome: ')
    pessoa['idade'] = int(input('Digite sua idade: '))
    pessoas.append(pessoa)
    for pessoa in pessoas:
        if pessoa['idade'] >= 18:
            print(pessoa['nome'], pessoa['idade'])
    

