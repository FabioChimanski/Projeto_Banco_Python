import sqlite3


banco = sqlite3.connect('banco_sistema.db')

cursor = banco.cursor()

#CRIAÇÃO TABELA USUARIO
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contas_bancarias (
        conta INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha INTEGER NOT NULL,
        saldo REAL DEFAULT 0
    );
""")

#CRIAÇÃO TABELA MOVIMENTAÇÕES
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movimentacao_conta (
        id_movimentacao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_conta INTEGER NOT NULL,
        tipo_operacao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_operacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_conta) REFERENCES Contas_bancarias(conta)
    );
""")


#REGISTRAR MOVIMENTAÇÕES
def registro_movimentacao(id_conta, tipo, valor):
    cursor.execute("""
        INSERT INTO Movimentacao_conta (id_conta, tipo_operacao, valor) VALUES (?, ?, ?)
""", (id_conta, tipo, valor))
    banco.commit()

#BUSCAR MOVIMENTAÇÕES (EXTRATO)
def buscar_extrato(id_conta):
    cursor.execute("SELECT * FROM Movimentacao_conta WHERE id_conta = ?", (id_conta,))
    return cursor.fetchall()#retorna todas as linhas localizadas

#CRIAR CONTA
def criar_conta(nome_usuario, senha_usuario):
    cursor.execute("INSERT INTO Contas_bancarias (nome, senha, saldo) VALUES (?, ?, 0)" ,(nome_usuario, senha_usuario) )
    banco.commit()
    
    print(f'Bem vindo {nome_usuario}! Sua conta foi criada com sucesso')

#ACESSAR CONTA
def acessar_conta(nome_usuario, senha_usuario):
    try:
        cursor.execute("SELECT * FROM Contas_bancarias WHERE nome = ? AND senha = ?" , (nome_usuario, senha_usuario))
        resultado = cursor.fetchone()
        return resultado
    except sqlite3.Error as e:
        print(f'Erro ao acessar sua conta! {e}')
    
#ATUALIZAR O SALDO
def atualizar_saldo(id_conta, novo_saldo):
    cursor.execute("UPDATE Contas_bancarias SET saldo = ? WHERE conta = ?" , (novo_saldo, id_conta))
    banco.commit()



#BUSCAR CONTA DESTINO TRANSFERENCIA
def buscar_conta_destino(numero_conta):
    cursor.execute("SELECT * FROM Contas_bancarias WHERE conta = ?", (numero_conta,))
    return cursor.fetchone()

#PROCESSAR TRANSFERENCIA
def processar_transferencia(id_origem, id_destino, valor):
    cursor.execute("UPDATE Contas_bancarias SET saldo = saldo - ? WHERE conta = ?", (valor, id_origem))
    cursor.execute("UPDATE Contas_bancarias SET saldo = saldo + ? WHERE conta = ?", (valor, id_destino))
    banco.commit()

