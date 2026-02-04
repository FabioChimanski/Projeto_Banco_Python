import Banco_Dados.database as db

class Conta:
    def __init__(self, conta, nome, senha, saldo):
        self.conta = conta
        self.nome = nome
        self.senha = senha
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print('Saldo insuficiente!')
            return False
    
    def depositar(self, valor):
        self.saldo += valor
        return True

