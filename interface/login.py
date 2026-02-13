import customtkinter as ctk
import Banco_Dados.database as db
from interface import menu

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        #Label para login
        self.label = ctk.CTkLabel(self, text="Login Banco", font=("Roboto", 24))
        self.label.pack(pady=20)

        #imput usuario
        self.input_usuario = ctk.CTkEntry(self, placeholder_text="Nome do usuario")
        self.input_usuario.pack(pady=10)

        #input senha
        self.input_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.input_senha.pack(pady=10)

        #Button
        self.btn_login = ctk.CTkButton(self, text="Acessar Conta", command=self.acao_do_botao)
        self.btn_login.pack(pady=20)

    #imprimir no terminal o usuario e senha
    def acao_do_botao(self):
        user = self.input_usuario.get()
        senha = self.input_senha.get()

        dados = db.acessar_conta(user, senha)

        if dados:
            print("Sucesso")

            janela_menu = menu.Menu(user) 

            self.destroy()
            
            janela_menu.mainloop()

        else:
            print('Usuario ou senha incorretos')


# Criamos a instância da sua classe
ap = Login()

# Objeto login


# 3. O loop que mantém a janela aberta
ap.mainloop()