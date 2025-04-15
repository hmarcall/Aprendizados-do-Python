
soma1 = 0
res = 0
while True:
    n1 = int(input('Digite um número inteiro (0 para sair): ')) 
    if n1 == 0:
        print(f'Programa encerrado.')
        break
    res=soma1+n1
    print(f'{n1} + {soma1} = {res}')
    soma1=res
