
import customtkinter

def clique():
    print('fazer Login')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela =customtkinter.CTk()
janela.geometry("500 x 300")

texto = customtkinter.CTkLabel(janela , text=" Fazer Login")
email = customtkinter.CTkEntry(janela ,placeholder_text="Email" )
senha =  customtkinter.CTkEntry (janela , placeholder_text= "Senha" , show ="*")

botao = customtkinter.CTkButton(janela , text=" Login" , command="clique")

texto.pack(padx = 10 , pady = 10)
email.pack(padx = 10 , pady = 10)
email.pack(padx = 10 , pady = 10)
senha.pack(padx = 10 , pady = 10)
botao.pack(padx = 10 , pady = 10)



janela.mainloop()
 

