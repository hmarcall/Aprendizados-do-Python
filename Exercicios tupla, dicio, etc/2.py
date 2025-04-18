lista=[]
for i in range(1, 6):
    digit = input('Digite um nome: ')
    lista.append(digit)
    lista.sort()
tupla = tuple(lista)
print (tupla)
