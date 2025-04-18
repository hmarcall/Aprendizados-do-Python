'''n1 = 1
while n1 <= 10:
    print(n1)
    n1 += 1


    
cont = 0  
while True:
    n1 = int(input('Digite um número inteiro (0 para sair): ')) 
    if n1 == 0:
        print(f'A soma dos números digitados é: {cont}')
        break
    cont += n1 

    

n1=7
while True:
    cont = int(input('Tente descobrir o numero: '))
    if cont == n1:
        print('Parabéns, você acertou!')
        break


        
for i in range(0,51,5):
    print(i)


    
n1 = int(input('Digite um numero: '))
while n1 != 0:
    print(n1)
    n1 -=1



senha = '1234'
senha1 = input('Digite a senha: ')
while senha != '1234':
    print('Senha Incorreta, tente novamente')
    if senha == '1234':
        print('Acesso Permitido')
        break




n1=1
soma=0
while n1<=100:
    if n1%2==0:
        soma+=n1
        print(soma)
    n1+=1
print(f'Soma total dos números pares de 1 a 100: {soma}')





n1, n2 = map(int,input('Digite uma sequencia de dois números: '))
print (f'{n2}{n1}')'''
