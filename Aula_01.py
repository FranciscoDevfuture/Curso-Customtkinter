#importando a biblioteca
import customtkinter as ctk

#criando a janela

janela = ctk.CTk()
#alterando tema para modo light
janela._set_appearance_mode('dark')
#criando um botão
btn = ctk.CTkButton(janela,text='Olá Mundo!')
#.pack() para fazer a aparecer o botao na tela
btn.pack()
#Executar janela
janela.mainloop()