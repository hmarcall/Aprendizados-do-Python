'''# Estruturas de Dados - Listas
'jogos=['GoW', 'RD2', 'TLoU', 'Valorant', 10, 2.5, True]
print (jogos)
jogos.append('Fifa=!CSGO')
print (jogos)
jogos[6] = 'COD'
print (jogos)




#APPEND
top_pornstars = []
for i in range(3):
    nome = input('Digite o seu top 3 pornstars: ')
    top_pornstars.append(nome)
print ('Seu top 3 pornstars: ', top_pornstars)




#EXERCICIO MEDIA DENTRO DA LISTA
media = []
soma=0
for i in range(5):
    nota= float(input('Digite: '))
    media.append(nota)
    soma += media[i]
media = soma/5
print (media)




#POP
celulares=['Samsung', 'Motorola', 'Apple', 'Xiaomi', 'LG']
print (celulares)
celulares[1:2] = ['Nokia', 'Sony']
print (celulares)
celulares.remove('Nokia')
print (celulares)
celulares.pop(1)
print (celulares)



#CONCATENAR LISTAS
roupas=['camiseta', 'calça', 'bermuda']
roupas2=['sapato', 'jaqueta']
roupas_combinadas = roupas + roupas2
print (roupas_combinadas)
print (len(roupas_combinadas))






#EXERCICIO ALEATORIO
cpf = input('Digite o CPF: ')
while True:
    if len(cpf)==11 and cpf.isdigit():
        print ('CPF válido')
    else:
        print ('CPF inválido')
        break 




#COPY
lista1=[1,2,3,4]
lista2= lista1.copy()
lista2.append(5)
print (lista1)
print (lista2)




#CLEAR
carrinho = ['celular', 'notebook', 'mouse']
carrinho.clear()
print (carrinho)



#USANDO O .SORT()
lista=[]
for i in range(1, 6):
    digit = input('Digite um nome: ')
    lista.append(digit)
    lista.sort()
print(lista)'''