print ('Ola, seja bem-vindo! Registre-se para continuar')
#if input('Caso ja possua cadastro digite "sim" para fazer login!') == 'sim':
digit1 = (str(input('Crie um UserName:')))
digit2 = (str(input('Crie uma Senha:')))
cadastro = {
    'username': digit1,
    'senha': digit2
}
print ('Seu cadastro foi realizado com sucesso!')
print ('Agora faça o login para continuar')
digit_Login = (str(input('Digite seu UserName:')))
digit_Senha = (str(input('Digite sua Senha:')))
for digit_Login in cadastro['username'] and digit_Senha in cadastro['senha']:
    print('Login realizado com sucesso')
    break
else:
    print('Login invalido. Tente novamente!')
