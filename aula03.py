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
#Executar janela
janela.mainloop()