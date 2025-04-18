#CRIANDO SETS (  ([])  ), (  {}  )
'''conjunto = {1, 2, 3, 4, 5}
print(conjunto)

conjunto = set({1, 2, 3, 4, 5})
for i in conjunto:
    print(i)'''


     
#USANDO DISCARD E .ADD
meu_Conjunto = set()
meu_Conjunto.add('Henrique')
for i in range(1,11):
    digitacao = str(input('Digite o nome que deseja adicionar a lista, ou digite "sair" em letras minúsculas para finalizar a lista: '))
    meu_Conjunto.add(digitacao)
    if digitacao == 'sair':
        meu_Conjunto.discard('sair')
        break
print(meu_Conjunto)



#UNIÃO, INTERSEÇÃO E DIFERENÇA DE CONJUNTOS
'''conj1 = {1, 2, 3}
conj2 = {3, 4, 5}
conj3 = {5, 6, 7}
uniao = conj1.union(conj2,conj3)
inter = conj1.intersection(conj2)
diferenca = conj1.difference(conj2)
diferenca2 = conj2.difference(conj1)
dif_Sim = conj1.symmetric_difference(conj2)
print(uniao)
print(inter)
print(diferenca)
print(diferenca2)
print(dif_Sim)



#ISSUBSET()
conj1 = {1, 2, 3}
conj2 = {1, 2, 3, 4, 5}
print(conj2.issubset(conj1))'''



