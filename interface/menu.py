import customtkinter as ctk
import Banco_Dados.database as db



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.title(f"Bem vindo {usuario}")
        self.geometry("600x400")

