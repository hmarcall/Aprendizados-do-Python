import tkinter as tk


janela = tk.Tk()
janela.title('My first window')
janela.geometry('1080x720')
label = tk.Label(janela, text = 'Look at here')
label.pack()
label1 = tk.Label(janela, text = 'Look at here 2')
label1.pack()
label2 = tk.Label(janela, text = 'Look at here 3')
label2.pack()
label3 = tk.Label(janela, text = '')
label3.pack()

entrada = tk.Entry(janela)
entrada.pack()



var = tk.IntVar()

def continuar():
    label = tk.Label(janela, bg='black', fg='white', text = 'Texto enviado!')
    label.pack()
    if botao.cget("text") :
        
        check = tk.Checkbutton(janela, text='Aceito os termos de uso do aplicativo', variable=var)
        check.pack()
          

def verificar():
    if var.get() == 0:
        print ('Aceite os termos para continuar!')
            
                
    
botao = tk.Button(janela, text='Clique aqui!', command=continuar)
botao.pack()

botao = tk.Button(janela, text='Acessar o site', command=verificar)
botao.pack()

        


    















janela.mainloop()