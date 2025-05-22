import mariadb
try:
    class PooDB:
        def __init__(self):

            self.conn = mariadb.connect(
                user = 'root',
                password = '',
                host = 'localhost',
                port = 3306,
                database = ''
            )
            self.cursor = self.conn.cursor()
            print("Conexão realizada com sucesso")

        def encerrar(self):
            self.conn.close()
            print("Conexão encerrada com sucesso")
except mariadb.Error as e:
    print (f'Erro ao conectar no Banco de dados:{e}') 