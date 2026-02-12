import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Olá")
        self.geometry("400x300")

        # 1. Criamos o objeto botão
        # 'self' diz que o botão pertence a esta janela
        # 'command' diz qual função rodar ao clicar
        self.btn = ctk.CTkButton(self, text="Clique Aqui", command=self.acao_do_botao)
        
        # 2. Posicionamos o botão na tela
        # O pack() é como colocar uma peça em uma caixa
        self.btn.pack(pady=20)

    def acao_do_botao(self):
        print("Botão pressionado!")

# Criamos a instância da sua classe
ap = App()

# 3. O loop que mantém a janela aberta
ap.mainloop()