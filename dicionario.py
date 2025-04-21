#APRENDENDO A USAR DICIONARIOS (del) 
'''dicionario= {
    'Nome': 'Henrique',
    'Idade': 19,
    'Cidade': 'São João del Rei',
    'Profissa': 'Programer'
}
print(dicionario['Nome'], dicionario['Idade'])
dicionario['Cidade'] = 'Rio de Janeiro'
print(dicionario)
del dicionario['Profissa']
print (dicionario)

#MESCLAR (.upgrade())
dicio = {
    'a': 1,
    'b': 2,
    'c': 3
}
dicio2 = {
    'c': 7,
    'd': 4,
    'e': 5
}
dicio.update(dicio2)
dicio2.update(dicio)
print (dicio)
print (dicio2)'''


#DICIONARIOS ANINHADOS E ITERAR (FOR)
'''dicio = {
    'pessoa1':{'Nome': 'Henrique', 'Idade': 19},
    'pessoa2':{'Nome': 'João', 'Idade': 20}
}
#print(dicio['pessoa1']['Nome'])
for chave in dicio:
    print(chave)

for valor in dicio.values():
    print(valor)

for chave, valor in dicio.items():
    print(chave, valor)                      



dicio = {
    'nome': 'Juju', 'idade': 19, 'cidade': 'São João del Rei', 'peso': 55.0
}
print(dicio)
dicio ['nome'] = 'Henrique'
dicio ['idade'] = 19
dicio ['cidade']= 'São João del Rei'
dicio ['peso']= 666.0
print (dicio)
dicio ['nome'] = str(input('Digite seu nome: '))
dicio ['idade'] = int(input('Digite seua idade: '))
dicio ['cidade']= str(input('Digite sua cidade: '))
dicio ['peso']= float(input('Digite seu peso: '))
print(dicio)

pessoas = []'''

pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Digite seu nome: ')
    pessoa['idade'] = int(input('Digite sua idade: '))

    pessoas.append(pessoa)
    
    parar = input('Deseja parar? Para parar digite "s", para continuar digite "n": ')
    if parar.lower() == 's':
        break

for i in pessoas:
    print(pessoas)

