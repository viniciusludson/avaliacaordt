from tkinter import*


janela= Tk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
    def tela(self):
        self.janela.title("Cadastro de clientes")
        self.janela.configure(background= "#1e3743")
        self.janela.geometry("700x500")
        self.janela.resizable(False, True)
        self.janela.maxsize(123, 765)
        self.janela.minsize(1234,1790)
    def frames_da_tela(self):
        self.frame_1= Frame(self.janela)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.8, relheight=0.89)
        self.frame_2=Frame(self.janela)
        self.frame_2.place(relx=0.09, rely=0.09, relwidth=0.049, relheight=0.74)

    def criando_botoes(self):
        self.bt_limpar=Button(self.frame_1)
        self.bt_limpar.place(relx=0.05, rely=0.005, relwidth=0.1, relheight=0.1)
        self.bt_novo=Button(self.frame_2)
        self.bt_novo.place(relx=0.01, rely=0.05, relwidth=0.62, relheight=0.10)



Application()
janela.mainloop()