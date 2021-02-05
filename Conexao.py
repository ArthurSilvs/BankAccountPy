import mysql.connector
def criar_conexao(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def fechar_conexao(con):
    return con.close()