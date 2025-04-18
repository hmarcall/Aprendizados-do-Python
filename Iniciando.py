"""print("hello world")
nome, preco = input('Digite seu nome e qual é preço do seu job:').split()
preço = float(preco)
print (f'Meu nome é:',nome, ', e o preço do meu job é R$:',preco)


n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
soma = n1 + n2
print(f'A soma de {n1} e {n2} é igual a {soma}')


n1 = float(input('digite:'))
n2 = float(input('digite:'))
media = (n1+n2)/2
print ('A média entre', n1 ,'e', n2, 'é igual a', media)


x = 'Henrique'
print (type(x))
x, y, z = 1, 2, 3
print(x,',', y,',' ,z)


n1 = float(input('digite:'))
n2 = float(input('digite:'))
multi = n1*n2
print ('A multiplicação entre', n1 ,'e', n2, 'é igual a', multi)

n1 = float(input('digite:'))
res = n1*2
print ('O dobro de', n1, 'é igual a', res)


n1 = float(input('digite:'))
n2 = float(input('digite:'))
n3 = float(input('digite:'))
media = (n1+n2+n3)/2
print ('A média entre', n1 ,'e', n2, 'e', n3, 'é igual a', media)


n1 = float(input('Digite: ')) 
print(f'O número {n1} é {("ímpar", "par")[int(n1) % 2 == 0]}.')


n1 = float(input('Digite: '))
n2 = float(input('Digite: '))
n3 = float(input('Digite: '))
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
     print('Os números formam um triângulo')
else:
     print('Não formam um triângulo')


n1 = int(input('Digite: ' ))
if n1 >=10 and n1<=50:
    print('Seu numero está seguindo as restrições do sistema corretamente!')
else: 
    print('Seu numero não está seguindo corretamente as restrições do sistema, tente novamente!')



n1 = int(input('Digite:'))
n2 = int(input('Digite:'))
if n1 == n2:
    print('Os números são iguais')
else: 
    print('Os números são diferentes')


n1 = float (input('Digite:'))
if n1 >0:
    print('Seu número é positivo')
elif n1 <0:
        print('Seu número é negativo')
else:
    print('Seu numero é zero')


n1 = int(input('Digite sua idade:'))
if n1>=16:
    print('Você pode votar')
else:
    print('Você não pode votar')


n1 = float(input('Digite um numero:'))
if n1 % 5 ==0:
    print('Seu número é multiplo por 5')
else:
    print('Seu numero não é multiplo de 5')


n1 = int(input('Digite: ' ))
if n1 >=1 and n1<=100:
    print('Seu numero está seguindo as restrições do sistema corretamente!')
else: 
    print('Seu numero não está seguindo corretamente as restrições do sistema, tente novamente!')



n1, n2, n3 = map(int, input('Digite tres numeros').split()) #USANDO MAP E SPLIT
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
medio = (n1+n2+n3) - (maior + menor)
print (f'Maior {maior}, Medio {medio}, Menor {menor}')


n1 = float (input('Digite seu salario: '))
if n1 < 2000:
    sreajuste1 = n1*(1+10/100)
    print(f' Seu salario apos o reajuste é de:{sreajuste1:.2f}')
else:
    sreajuste2 = n1*(1+5/100)
    print(f'Seu salario apos o reajuste é de:{sreajuste2:.2f}')



peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'O seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 24.9:
    print('Você está no peso ideal')
else:
    print('Você está com acima do peso')


nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('Você foi aprovado!')
elif 5 <= nota <= 6.9:
    print('Você está de recuperação')
else: 
    print('Você foi reprovado!')


ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')


n1 = int(input('Digite um numero de correspondente ao dia da semana que deseja:'))
if n1 == 1:
    print('Segunda-feira')
elif n1 == 2:
    print('Terça-feira')
elif n1 == 3:
    print ('Quarta-feira')
elif n1 == 4:
    print('Quinta-feira')
elif n1 == 5:
    print('Sexta-feira')
elif n1 == 6:
    print('Sábado')
elif n1 >=7:
    print('Dia da semana inválido')


nome1 = "Henrique"
senha1 = "123"
nome = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
if (nome1 and senha1) != (nome and senha):
    print('Usuário e senha incorretos')
else:
    print('Login bem sucedido')"""

