import customtkinter as ctk

def Flogin():
    user = entry1.get()
    senha = entry2.get()
    if user == 'hmarcall' and senha == 'minato':
        label3.configure(text= 'Sucssesfuly login', text_color="green")
    else:
        label3.configure(text= 'Try again', text_color="red")


ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('CTk teste')
janela.geometry('1080x720')

label = ctk.CTkLabel(janela, text='Usuario:', font=('Calibri', 20, 'bold'))
label.grid(row=6, column=0, padx=402, pady=(100,1), sticky='w')

entry1 = ctk.CTkEntry(janela, placeholder_text='Digite o seu nome de usuario:')
entry1.grid(row=7, column=0, padx=400, pady=(1,7), sticky='we')

label2 = ctk.CTkLabel(janela, text='Senha:', font=('Calibri', 20, 'bold'))
label2.grid(row=8, column=0, padx=402, pady=(10,1), sticky='w')

entry2 = ctk.CTkEntry(janela, placeholder_text='Digite sua senha:', show='*')
entry2.grid(row=9, column=0, padx=400, pady=(1,7), sticky='we')

botao = ctk.CTkButton(janela, text='LOGIN', command=Flogin)
botao.grid(row=10, column=0, padx=470, pady=(10,7), sticky='w')

label3 = ctk.CTkLabel(janela, text='')
label3.grid(row=11, column=0, padx=470, pady=(10,0), sticky='w')

janela.mainloop()