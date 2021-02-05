from Conexao import criar_conexao, fechar_conexao

class Conta:
    def __init__(self, nome, idade, nmrconta):
        self.nome = nome
        self.idade = idade
        self.nmrconta = nmrconta
        self.saldo = 00.0

    def get_dados(self):
        print(f'Nome = {self.nome}, Idade = {self.idade}, Número da conta = {self.nmrconta}, Saldo da Conta = {self.saldo}')


    def cadastrar(self, nmrconta, nome, idade):
        con = criar_conexao("localhost", "root", "", "conta_bancaria")
        cursor = con.cursor()
        sql = "INSERT INTO clientes (nmrconta, nome, idade, saldo) values (%s, %s, %s, %s)"
        valores = (self.nmrconta, self.nome, self.idade, self.saldo)
        cursor.execute(sql, valores)
        cursor.close()
        con.commit()
        fechar_conexao(con)

    @staticmethod
    def depositar(nmrc, valor):
        nmr = nmrc
        con = criar_conexao("localhost", "root", "", "conta_bancaria")
        cursor = con.cursor()
        sql = "SELECT nome, saldo FROM clientes WHERE nmrconta = %s"
        cursor.execute(sql, (nmr, ))
        for (nome, saldo) in cursor:
            print(nome, saldo)
        ad = saldo + valor
        up = "UPDATE clientes SET saldo = %s WHERE nmrconta = %s"
        cursor.execute(up, (ad, nmr, ))
        print("Deposito realizado com sucesso! Saldo atual da Conta: R$", ad)
        cursor.close()
        con.commit()
        fechar_conexao(con)

    @staticmethod
    def sacar(nmrc, valor):
        nmr = nmrc
        con = criar_conexao("localhost", "root", "", "conta_bancaria")
        cursor = con.cursor()
        sql = "SELECT nome, saldo FROM clientes WHERE nmrconta = %s"
        cursor.execute(sql, (nmr,))
        for (nome, saldo) in cursor:
            print(nome, saldo)
        if valor < saldo:
            newsaldo = saldo-valor
            up = "UPDATE clientes SET saldo = %s WHERE nmrconta = %s"
            cursor.execute(up, (newsaldo, nmrc, ))
            print("Saque realizado com sucesso! Saldo atual da Conta: R$", newsaldo)
        else:
            print("Erro: Saldo insuficiente!")
        cursor.close()
        con.commit()
        fechar_conexao(con)

