import mariadb
try:
    conn = mariadb.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        port = 3306,
        database = 'teste_db'
    )

    cursor = conn.cursor()
    while True:
        usuarios = {
            'nome': input('Digite o nome do usuario: '),
            'idade': int(input('Digite a idade do usuario: ')),
            'sobrenome': input('Digite o sobrenome do usuario: '),
            'cidade': input('Digite a cidade do usuario: ')
        } 
        if input('Deseja continuar? (s/n): ').lower() == 'n':
            break

    cursor.executemany(
        "INSERT INTO usuario (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)", 
        (
        usuarios['nome'],
        usuarios['idade'],
        usuarios['sobrenome'],
        usuarios['cidade']
        )
    )
    
    conn.commit()
    print('Dados inseridos com sucesso!')
    conn.close()
    

except mariadb.Error as e:
    print('Erro ao conectar no banco de dados:', e)
