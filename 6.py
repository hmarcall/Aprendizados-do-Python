frutas=['butikabah', 'banana']
legumes=['djiloh', 'cenoura']
digitacao=str(input('Digite o nome de um alimento: '))
if digitacao in frutas:
    print('Você digitou uma fruta')
elif digitacao in legumes:
    print('Você digitou um legume')
else:
    print('O alimento que você digitou não está em nenhuma das listas')
