import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import messagebox
import customtkinter as ctk
import _tkinter as tk
from Conexoes_db.Estoque.estoque import Produto
from Conexoes_db.Estoque.conn_estoque import PooDB

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('Estoque')
janela.geometry('1080x720')

banco = PooDB()

def cadastrar_produto():
    nome = entry1.get()
    quantidade = entry2.get()
    categoria = entry3.get()
    descricao = entry4.get()
    if not nome or not quantidade or not categoria or not descricao:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    produto = Produto(nome, quantidade, categoria, descricao)
    produto.inserir(banco)
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')

label = ctk.CTkLabel(janela, text='Cadastrar novo produto:', font=('Calibri', 20, 'bold'))
label.grid(row=1, column=0, padx=402, pady=(100,1), sticky='w')

entry1 = ctk.CTkEntry(janela, placeholder_text='Digite o nome do produto:')
entry1.grid(row=2, column=0, padx=400, pady=(1,7), sticky='we')

entry2 = ctk.CTkEntry(janela, placeholder_text='Digite a quantidade do produto:')
entry2.grid(row=3, column=0, padx=400, pady=(1,7), sticky='we')

entry3 = ctk.CTkEntry(janela, placeholder_text='Digite a categoria do produto:')
entry3.grid(row=4, column=0, padx=400, pady=(1,7), sticky='we')

entry4 = ctk.CTkEntry(janela, placeholder_text='Digite a descrição do produto:')
entry4.grid(row=5, column=0, padx=400, pady=(1,7), sticky='we')

botao_cadastrar = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_produto)
botao_cadastrar.grid(row=6, column=0, padx=400, pady=(10, 10), sticky='we')

janela.mainloop()