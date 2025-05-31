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

    usuarios = []
    
    while True:
        nome = input('Digite o nome do usuario: ')
        idade = int(input('Digite a idade do usuario: '))
        sobrenome = input('Digite o sobrenome do usuario: ')
        cidade = input('Digite a cidade do usuario: ')
        
        # Adiciona os dados como uma lista
        usuarios.append((nome, idade, sobrenome, cidade))
        
        if input('Deseja continuar? (s/n): ').lower() == 'n':
            break
    
    print(usuarios)

    cursor.executemany(
        "INSERT INTO usuario (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)", usuarios)
    
    conn.commit()
    conn.close()
    print('Dados inseridos com sucesso!')

except mariadb.Error as e:
    print('Erro ao conectar no banco de dados:', e)
