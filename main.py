import tkinter as tk
janela= tk.Tk()
janela.title("My lovely Jake")
janela.geometry("300x765")
def botao_salvar():
    label_nome=entry.get()
    print(f"Nome digitado:{label_nome}")

#criando yuma outra def para retornar o valor digitado
def retornar_valor():
    label_nome=entradas.get()
    print(f"Valor retornado:{label_Endereco}")


label_nome=tk.Label(janela,text="Nome:", width="12",font="Arial,12")
label_nome.pack()
label_Endereco=tk.Label(janela,text="Endereço:",font="Arial,14")
label_Endereco.pack()
#criando entradas
entradas=tk.Entry(janela )
entradas.pack()
label_nome=tk.Entry(janela, text="")
label_nome.pack()
#criando botoes
botao_salvar=tk.Button(janela,text="Salvar",command=botao_salvar)
botao_salvar.pack()
botao_retornar=tk.Button(janela, text="Retornar Valor", command=retornar_valor)
botao_retornar.pack()

label=tk.Label(janela,text="")
label.pack()
janela.mainloop()