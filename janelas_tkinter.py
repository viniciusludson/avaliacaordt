#Instalando a biblioteca tkinter
import os
from datetime import datetime
from tkinter import *   #importando a biblioteca Tkinter
from  tkinter.ttk import Combobox
janela = Tk() #chamando a janela
janela.title(" Cadastro ")
janela.geometry("400x300")
janela.configure(bg="#D3D3D3")


#Funções do programa

def Cadastrar_usuario():
    novo=caixa_nome.get()
    resultado= Label(janela, text='Nome: ' +a, font="Arial 20", fg="#27DAF5", bg="#27DAF5")
    resultado.place(x=20, y=400)
    print(novo)


# JANELA DE CADASTRO DE PESSOAS  .get() capturar o nome

nome1= Label(text="Nome: ", font="Arial 18", fg="#8027F5")  #fg= cor da frase
nome1.place(x=20, y=20)

caixa_nome=Entry(font="Arial 20")
caixa_nome.place(x=150, y=20)

Endereco= Label(text="Endereço: ", font="Arial 18", fg="#8027F5")
Endereco.place(x= 20, y=60)

caixa_endereco=Entry(font="Arial 20")
caixa_endereco.place(x=150, y=67)

Bairro= Label(text="Bairro: ", font="Arial 18", fg="#8027F5")
Bairro.place(x=20, y=120)

caixa_bairro=Entry(font="Arial 20")
caixa_bairro.place(x=150, y=115)

Estado=Label(text="Estado: ", font="Arial 18", fg="#8027F5")
Estado.place(x=20, y=160)

#criando combobox uma janelinha de opcoes no menu

estado= Label(text="Estado: ", font="Arial 20", fg="#8027F5")
estado.place(x=20, y=160)

combo=Combobox(janela, font="black")
combo.place(x=150, y=160)
combo["values"]= ["MA", "PI", "CE", "MT", "RN"]

telefone=Label(text="Telefone: ", font="Arial 20", fg="#8027F5")
telefone.place(x=20, y=195)

caixa_telefone=Entry(font="Arial 20")
caixa_telefone.place(x=150, y=195)

email=Label(text="Email: ", font="Arial 18", fg="#8027F5")
email.place(x=20, y=240)

caixa_email=Entry(font="Arial 18")
caixa_email.place(x=150, y=240)

celular=Label(text="Celular: ", font="Arial 18", fg="#8027F5")
celular.place(x=20, y=280)

caixa_celular=Entry(font="Arial 20")
caixa_celular.place(x=150, y=280)









#Criando botao
botao_gravar=Button(text="Gravar Cadastro",font="Arial 18")
botao_gravar.place(x=20, y=400)

novo_cadastro=Button(text="Novo Cadastro",font="Arial 18")
novo_cadastro.place(x=280, y=400)

ver_cadastro=Button(text="Ver cadastro",font="Arial 18")
ver_cadastro.place(x=520, y=400)





janela.mainloop() #para poder rodar a janela

#atividade de casa: fazer a janela