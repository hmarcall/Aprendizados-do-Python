conj = set()
conj2 = set()
for i in range (1,6):
    digit = int(input('Digite um numero inteiro para adicionar ao conjunto: '))
    conj.add(digit)
print(conj)
for i in range (1,6):
    digit1 = int(input('Digite um numero inteiro para adicionar ao conjunto: '))
    conj2.add(digit1)
print (conj2)
if conj.intersection(conj2):
    print ('Os elemntos em comum são', conj.intersection(conj2))
else: 
    print ('Não há elementos em comum')
