'''from Conexao import criar_conexao, fechar_conexao

def inserir_cliente(con, nome, idade, nmrconta, saldo):
    cursor = con.cursor()
    sql = "INSERT INTO clientes (nmrconta, nome, idade, saldo) values (%s, %s, %s, %s)"
    valores = (nmrconta, nome, idade, saldo)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def show_all(con):
    cursor = con.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)

    for (nmrconta, nome, idade, saldo) in cursor:
        print(nmrconta, nome, idade, saldo)

    cursor.close()

def main():
    con = criar_conexao("localhost", "root", "", "conta_bancaria")

    show_all(con)

    #inserir_cliente(con, "teste", 16, 4441, 5)

    fechar_conexao(con)

if __name__ == "__main__":
    main()'''

from Conta import Conta
from random import randint

print('Bem-vind@ ao Banco Nacional do Arthur')
print("""
        1 - Criar Conta
        2 - Depositar
        3 - Sacar 
    """)
op = int(input('Qual operação deseja realizar? '))

while (op < 1) or (op > 3):
    op = int(input('Opção incorreta, digite uma opção válida: '))

if op == 1:
    print("Abrir Conta Bancária")
    nome = input("Digite o nome: ")
    idade = input("Digite a Idade: ")
    nmrconta = randint(1000, 9999)
    c1 = Conta(nome, idade, nmrconta)
    c1.cadastrar(nome, idade, nmrconta)

elif op == 2:
    print('Depósito')
    nmrc = int(input('Digite o número da conta: '))
    valor = float(input('Digite o valor: '))
    Conta.depositar(nmrc, valor)

elif op == 3:
    print('Saque')
    nmrc = int(input('Digite o número da conta: '))
    valor = float(input('Digite o valor: '))
    Conta.sacar(nmrc, valor)

else:
    print('Operação Cancelada')
