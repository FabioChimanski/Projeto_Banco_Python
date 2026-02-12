#Ponto de partida do software
import Banco_Dados.database as db
from modelos.conta import Conta

opcao = ""

while True:
    print('BANCO')
    print('================')
    print('1 - cadastro: ')
    print('2 - acessar conta: ')
    print('0 - sair sistema')
    print('================')
    opcao = input('opção: ')
    match opcao:

        #CADASTRO
        case "1": 
            print('Bem vindo!')
            nome_usuario = input('Informe seu nome: ')
            senha_usuario = input('Informe sua senha usando apenas 4 digitos')
            db.criar_conta(nome_usuario, senha_usuario)

        #LOGIN
        case "2":
            usuario = input('Usuario: ')
            senha = input('Senha: ')
            dados = db.acessar_conta(usuario, senha)
            
            if dados:

                conta_login = Conta(dados[0], dados[1], dados[2], dados[3])

                print(f'Bem vindo {dados[1]}!')
                while True:
                    print('================')
                    print('1 - Extrato: ')
                    print('2 - Saldo: ')
                    print('3 - Saque ')
                    print('4 - Depositar: ')                    
                    print('5 - Transferir: ')
                    print('0 - Sair: ')
                    print('================')
                    opcao_usuario = input('')

                    match opcao_usuario:

    

                        #EXTRATO
                        case "1":
                            print('EXTRATO')
                            movimentacoes = db.buscar_extrato(conta_login.conta)

                            if movimentacoes:
                                for mov in movimentacoes:
                                    print(f"{mov[4]} | {mov[2]:<15} | R${mov[3]:>8.2f}")
                            else:
                                print('Sem registro até o momento!')
                            
                        #SALDO
                        case "2":
                            print('SALDO')
                            print(f'Saldo: R${conta_login.saldo:.2f}')
                        #SAQUE
                        case "3":
                            print('SAQUE')

                            valor_saque = float(input('Informe o valor R$ '))
                            
                            if conta_login.sacar(valor_saque):
                                db.atualizar_saldo(conta_login.conta, conta_login.saldo)
                                db.registro_movimentacao(conta_login.conta, "SAQUE", valor_saque)
                                print(f'Saque realizado com sucesso! Saldo atual R${conta_login.saldo:.2f}')
                        
                        #DEPOSITO
                        case "4":
                            print('DEPOSITO')

                            valor_deposito = float(input('Informe o valor R$ '))

                            if conta_login.depositar(valor_deposito):
                                db.atualizar_saldo(conta_login.conta, conta_login.saldo)
                                db.registro_movimentacao(conta_login.conta, "DEPOSITO", valor_deposito)
                                print(f'Deposito no valor de {valor_deposito} realizado com sucesso!')

                        #TRANSFERIR
                        case "5":
                            print('TRANSFERIR')
                                                    
                            conta_dest = input('Digite o numero da conta destino: ')
                            valor_transf = float(input('Valor da transferencia: '))

                            if conta_login.sacar(valor_transf):
                                destino = db.buscar_conta_destino(conta_dest)

                                if destino:
                                    db.processar_transferencia(conta_login.conta, conta_dest, valor_transf)
                                    db.registro_movimentacao(conta_login.conta, "TRANSFERENCIA", valor_transf)
                                    print(f'Transferencia de R$ {valor_transf} para {destino[1]} realizada com sucesso!')
                                else:
                                    conta_login.depositar(valor_transf)
                                    print('Conta destino não encontrada!')

                        #SAIR
                        case "0":
                            break



        case "0":
            print('Até logo!')
            break
