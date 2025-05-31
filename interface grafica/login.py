from tkinter import messagebox
import customtkinter as ctk
import _tkinter as tk
from PIL import Image

imagem_pil = Image.open(r'D:\Users\983297\Python\Aprendizados-do-Python\Aprendizados-do-Python\interface grafica\eren.jpeg')
imagem_ctk = ctk.CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(100, 100))

def Flogin():
    user = entry1.get()
    senha = entry2.get()
    if user == 'hmarcall' and senha == 'minato':
        label3.configure(text='Login successful', text_color="green")
    else:
        label3.configure(text='Try again', text_color="red")

def ver():
    if check_var.get():
        entry2.configure(show='')
    else:
        entry2.configure(show='*')

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('CTk teste')
janela.geometry('1080x720')

label_img = ctk.CTkLabel(janela, image=imagem_ctk, text='')
label_img.grid(row=5, column=0, padx=450, pady=(80,7))

label = ctk.CTkLabel(janela, text='Usuario:', font=('Calibri', 20, 'bold'))
label.grid(row=6, column=0, padx=402, pady=(10,1), sticky='w')

entry1 = ctk.CTkEntry(janela, placeholder_text='Digite o seu nome de usuario:')
entry1.grid(row=7, column=0, padx=400, pady=(1,7), sticky='we')

label2 = ctk.CTkLabel(janela, text='Senha:', font=('Calibri', 20, 'bold'))
label2.grid(row=8, column=0, padx=402, pady=(10,1), sticky='w')

botao = ctk.CTkButton(janela, text='LOGIN', command=Flogin)
botao.grid(row=10, column=0, padx=402, pady=(10,7), sticky='w')

entry2 = ctk.CTkEntry(janela, placeholder_text='Digite sua senha:', show='*')
entry2.grid(row=9, column=0, padx=400, pady=(1,7), sticky='we')

check_var = ctk.BooleanVar()
checkbox = ctk.CTkCheckBox(janela, text='', variable=check_var, command=ver)
checkbox.grid(row=9, column=0, padx=540, pady=(10), sticky='w')

label3 = ctk.CTkLabel(janela, text='')
label3.grid(row=11, column=0, padx=470, pady=(10,0), sticky='w')

janela.grid_rowconfigure((0,1), weight=0)
janela.grid_columnconfigure((0,1), weight=0)

janela.mainloop()