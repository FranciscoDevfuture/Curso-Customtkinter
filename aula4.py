#importando a biblioteca
import customtkinter as ctk

#criando a janela
janela = ctk.CTk()
#alterando o título
janela.title('Criando minha janela By Francisco Version 1.0')
#definindo as dimensões da janela
janela.geometry('400x200')
janela.maxsize(width=900,height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True,height=False)

#custumizando tema da nossa aplicação
janela._set_appearance_mode('system')

#criando uma nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color='teal')# recebe apenas um parametro
    nova_janela.geometry('500x250')
    
btn_novatela = ctk.CTkButton(master=janela, text='abrir nova janela',command=nova_tela).place(x=200, y=100)



#Executar janela
janela.mainloop()