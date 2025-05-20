import mariadb
try:
    conn =mariadb.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        port = 3306,
        database = 'teste_db'
    )

    cursor = conn.cursor()




    usuarios = []
    while True:
        digit = input( 'Digite seus dados no seguinte formato: nome, idade, sobrenome, cidade. \n' \
        'Caso queira encerrar a inserção de dados no sistema digite "0"\n' \
        'DIGITE AQUI OS DADOS:')
        if digit == '0':
            print ('Os usuarios foram adicionados ao sistema!')
            break

        dados = [campo.strip() for campo in digit.split(',')] # Dividir e limpar os dados
        
        if len(dados) != 4:
            print(' Por favor, digite exatamente 4 campos separados por vírgula.')
            continue

    usuarios.append(dados)


    cursor.executemany(
        "INSERT INTO usuario (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)",
        usuarios
    )
    conn.commit()

except mariadb.Error as e:
    print ('Erro ao conectar no banco de dados', e)
