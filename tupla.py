'''
# TUPLAS
letras=('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
print (letras)


numeros=(1,2,3)
a,b,c = numeros
print (c)


# SUM (SOMA DOS ELEMENTOS DA TUPLA)
tupla = (0,2,4,6,8,10)
print (tupla)
print (tupla[0])
print (tupla[-1])
print (sum(tupla))

#TUPLE IN TUPLE
cidades =(
    ('São João del Rei', '21° 08′ 09″ S', '-44° 15′ 43″ O'),
    ('Rio de Janeiro', '22° 54′ 10″ S', '-43° 12′ 28″ O'),
    ('Fortaleza', '3° 43′ 58″ S', '38° 31′ 37″ O'),
    ('Central Park, NY', '40° 46′ 56″ N', '-73° 57′ 55″ O')
)
local=cidades[0][0:2]
print (local)


# CONVERTENDO TUPLAS EM LISTAS OU VICE-VERSA
lista = [1,2,3,4,5]
print (lista)

tupla = tuple(lista)
print (tupla)

lista = list(tupla)
print (lista)







#EXERCICIO TUPLA
tupla = ('Henrique', 'Guilherme', 'Lucas', 'Gabriel', 'Pedro', 'João', 'Matheus', 'Rafael',)
lista = list(tupla)
while True:
    print ('Adicione um nome à lista ou digite "sair" para sair: ')
    digitacao = str(input('Digite o nome que deseja adicionar a lista: '))
    dl = digitacao.lower()
    lista.append(dl)
    if dl == 'sair':
        lista.remove('sair')
        break
tupla = tuple(lista)
print(tupla)'''\
