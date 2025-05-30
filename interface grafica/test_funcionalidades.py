from tkinter import messagebox
import customtkinter as tk



janela = tk.CTk()
janela.title('My first window')
janela.geometry('1080x720')
label = tk.CTkLabel(janela, text='Look at here')
label.pack()
label1 = tk.CTkLabel(janela, text='Look at here 2')
label1.pack()
label2 = tk.CTkLabel(janela, text='Look at here 3')
label2.pack()
label3 = tk.CTkLabel(janela, text='')
label3.pack()

entrada = tk.CTkEntry(janela)
entrada.pack()

var = tk.IntVar()

def continuar():
    label = tk.CTkLabel(janela, fg_color='black', text_color='white', text='Texto enviado!')
    label.pack()
    if botao.cget("text"):
        check = tk.CTkCheckBox(janela, text='Aceito os termos de uso do aplicativo', variable=var)
        check.pack()

def verificar():
    if var.get() == 0:
        print('Aceite os termos para continuar!')

botao = tk.CTkButton(janela, text='Clique aqui!', command=continuar)
botao.pack()

botao2 = tk.CTkButton(janela, text='Acessar o site', command=verificar)
botao2.pack()

opcao = tk.StringVar()
opcao.set('')

radio1 = tk.CTkRadioButton(janela, text='first option', variable=opcao, value='1')
radio2 = tk.CTkRadioButton(janela, text='second option', variable=opcao, value='2')

radio1.pack()
radio2.pack()

def alerta():
    messagebox.showinfo('Alerta','Login bem sucedido!')

botao3 = tk.CTkButton(janela, text='Alert', command=alerta)
botao3.pack()


#*Não roda por que minha "janela" usa o pack() e o frame esta usando o grid()*
'''def botao1():
    pass
frame=tk.CTkFrame(master=janela, corner_radius=10)
frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
botao4=tk.CTkButton(master=frame, text='Butãozin', command=botao1)
botao4.pack(padx=20, pady=20)'''


janela.grid_rowconfigure((0,1), weight=1)
janela.grid_columnconfigure((0,1), weight=1)


janela.mainloop()