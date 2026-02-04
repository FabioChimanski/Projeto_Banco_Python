import sqlite3


banco = sqlite3.connect('banco_sistema.db')

cursor = banco.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contas_bancarias (
        conta INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha INTEGER NOT NULL,
        saldo REAL DEFAULT 0
    );
""")


def criar_conta(nome_usuario, senha_usuario):
    cursor.execute("INSERT INTO Contas_bancarias (nome, senha, saldo) VALUES (?, ?, 0)" ,(nome_usuario, senha_usuario) )
    banco.commit()
    
    print(f'Bem vindo {nome_usuario}! Sua conta foi criada com sucesso')

def acessar_conta(nome_usuario, senha_usuario):
    try:
        cursor.execute("SELECT * FROM Contas_bancarias WHERE nome = ? AND senha = ?" , (nome_usuario, senha_usuario))
        resultado = cursor.fetchone()
        return resultado
    except sqlite3.Error as e:
        print(f'Erro ao acessar sua conta! {e}')
    
def atualizar_saldo(id_conta, novo_saldo):
    cursor.execute("UPDATE Contas_bancarias SET saldo = ? WHERE conta = ?" , (novo_saldo, id_conta))
    banco.commit()

def saldo():
    pass
 
def transferencia():
    pass

def saque():
    pass

def extrato():
    pass