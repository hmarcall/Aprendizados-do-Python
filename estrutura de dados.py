'''jogos=['GoW', 'RD2', 'TLoU', 'Valorant', 10, 2.5, True]
print (jogos)
jogos.append('Fifa=!CSGO')
print (jogos)
jogos[6] = 'COD'
print (jogos)




top_pornstars = []
for i in range(3):
    nome = input('Digite o seu top 3 pornstars: ')
    top_pornstars.append(nome)
print ('Seu top 3 pornstars: ', top_pornstars)




media = []
soma=0
for i in range(5):
    nota= float(input('Digite: '))
    media.append(nota)
    soma += media[i]
media = soma/5
print (media)




celulares=['Samsung', 'Motorola', 'Apple', 'Xiaomi', 'LG']
print (celulares)
celulares[1:2] = ['Nokia', 'Sony']
print (celulares)
celulares.remove('Nokia')
print (celulares)
celulares.pop(1)
print (celulares)




roupas=['camiseta', 'calça', 'bermuda']
roupas2=['sapato', 'jaqueta']
roupas_combinadas = roupas + roupas2
print (roupas_combinadas)
print (len(roupas_combinadas))







cpf = input('Digite o CPF: ')
while True:
    if len(cpf)==11 and cpf.isdigit():
        print ('CPF válido')
    else:
        print ('CPF inválido')
        break    '''  

