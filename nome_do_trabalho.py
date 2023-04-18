from tkinter import *
#IMPORTAR O TKINTER


class NomeDaClass:
    #CLASSE COM O NOME
    vermelho = '#d00000'
    vermelho_escuro = '#9d0208'
    vermelho_claro = '#ff006e'
    laranja = '#e85d04'
    laranja_normal = '#fb5607'
    amarelo = '#ffee32'
    amarelo_escuro = '#ffd100'
    verde = '#70e000'
    verde_escuro = '#008000'
    verde_claro = '#9ef01a'
    azul = '#48cae4'
    acul_escuro = '#023e8a'
    azul_claro = '#90e0ef'
    roxo = '#8338ec'
    roxo_escuro = '#5a189a'
    roxo_claro = '#c77dff'
    branco = '#ffffff'
    preto = '#000000'
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#d00000'
    #CORES

    def __init__(self):
        #DEFIÇÃO PRINCIPAL
        self.root = Tk()
        self.config()
        #CONFIGURAÇÃO DA TELA
        self.margem()
        #MARGEM DA TELA
        self.frames()
        #TELAS PRINCIPAIS
        self.widgets()
        #IMAGENS E TEXTOS PRINCIPAIS

        self.root.mainloop()

    def config(self):
        self.root.configure(background=self.cor1)
        self.root.state('zoomed')
        #CONFIGURAÇÃO

    def margem(self):
        self.frame_central = Frame(self.root, bg=self.cor2)
        self.frame_central.place(relx=0.0025, rely=0.005, relwidth=0.995, relheight=0.99)

        self.frame_central2 = Frame(self.root, bg=self.cor1)
        self.frame_central2.place(relx=0.0075, rely=0.015, relwidth=0.985, relheight=0.97)

        self.frame_central3 = Frame(self.root, bg=self.cor3)
        self.frame_central3.place(relx=0.0095, rely=0.019, relwidth=0.981, relheight=0.961)
        #MARGEM

    def frames(self):
        
        self.frame_principal1 = Frame(self.root, bg=self.cor2)
        self.frame_principal1.place(relwidth=0.958, relheight=0.696, relx=0.021, rely=0.041)

        self.frame_principal2 = Frame(self.root, bg=self.cor1)
        self.frame_principal2.place(relwidth=0.95, relheight=0.68, relx=0.025, rely=0.05)

        self.frame_principal3 = Frame(self.root, bg=self.cor2)
        self.frame_principal3.place(relwidth=0.958, relheight=0.176, relx=0.021, rely=0.777)

        self.frame_principal4 = Frame(self.root, bg=self.cor1)
        self.frame_principal4.place(relwidth=0.95, relheight=0.16, relx=0.025, rely=0.785)
        #IMAGENS DE "vackground"

    def widgets(self):
        self.load_img1 = PhotoImage(file='images/botao1.png')
        self.load_img2 = PhotoImage(file='images/botao2.png')
        self.load_img3 = PhotoImage(file='images/botao3.png')
        self.load_img4 = PhotoImage(file='images/botao4.png')
        self.load_img5 = PhotoImage(file='images/botao5.png')
        self.load_img6 = PhotoImage(file='images/trash.png')
        self.load_img7 = PhotoImage(file='images/close.png')
        #IMAGENS USADAS PARA OS BOTÕES

        self.info1 = Button(self.frame_principal4, image= self.load_img1, bg = self.cor1, activebackground = self.cor1, border=0, command = self.mostrar1)
        self.info1.place(relx=0.0005, rely=0.11)

        self.info2 = Button(self.frame_principal4, image= self.load_img2, bg = self.cor1, activebackground = self.cor1, border=0, command = self.mostrar2)
        self.info2.place(relx=0.075, rely=0.11)

        self.info3 = Button(self.frame_principal4, image= self.load_img3, bg = self.cor1, activebackground = self.cor1, border=0, command = self.mostrar3)
        self.info3.place(relx=0.15, rely=0.11)

        self.info4 = Button(self.frame_principal4, image= self.load_img4, bg = self.cor1, activebackground = self.cor1, border=0, command = self.mostrar4)
        self.info4.place(relx=0.225, rely=0.11)

        self.info5 = Button(self.frame_principal4, image= self.load_img5, bg = self.cor1, activebackground = self.cor1, border=0, command = self.mostrar5)
        self.info5.place(relx=0.3, rely=0.11)

        self.lixo = Button(self.frame_principal4, image= self.load_img6, bg = self.cor1, activebackground = self.cor1, border=0, command = self.limpar)
        self.lixo.place(relx=0.9, rely=0.11)

        self.fechar = Button(self.frame_principal4, image= self.load_img7, bg = self.cor1, activebackground = self.cor1, border=0, command = self.sair)
        self.fechar.place(relx=0.825, rely=0.11)
        #LIMPAR INFORMAÇÕES DA TELA



    def mostrar1(self):
        self.limpar()
        self.image1 = PhotoImage(file='images/botao1.png')
        self.imagem1= Label(self.frame_principal2, image = self.image1, bg = self.cor1)
        self.imagem1.place(relx=0.05, rely=0.12)
        self.txt_info1 = Label(self.frame_principal2, text='INFO1', bg = self.cor1, fg = self.cor2, font=('arial', 20))
        self.txt_info1.place(relx=0.55, rely=0.1)
        #COMANDO PARA USAR NO BOTÃO

    def mostrar2(self):
        self.limpar()
        self.image2 = PhotoImage(file='images/botao2.png')
        self.imagem2= Label(self.frame_principal2, image = self.image2, bg = self.cor1)
        self.imagem2.place(relx=0.05, rely=0.12)
        self.txt_info2 = Label(self.frame_principal2, text='INFO2', bg = self.cor1, fg = self.cor2, font=('arial', 20))
        self.txt_info2.place(relx=0.55, rely=0.1)
        #COMANDO PARA USAR NO BOTÃO

    def mostrar3(self):
        self.limpar()
        self.image3 = PhotoImage(file='images/botao3.png')
        self.imagem3= Label(self.frame_principal2, image = self.image3, bg = self.cor1)
        self.imagem3.place(relx=0.05, rely=0.12)
        self.txt_info3 = Label(self.frame_principal2, text='INFO3', bg = self.cor1, fg = self.cor2, font=('arial', 20))
        self.txt_info3.place(relx=0.55, rely=0.1)
        #COMANDO PARA USAR NO BOTÃO

    def mostrar4(self):
        self.limpar()
        self.image4 = PhotoImage(file='images/botao4.png')
        self.imagem4= Label(self.frame_principal2, image = self.image4, bg = self.cor1)
        self.imagem4.place(relx=0.05, rely=0.12)
        self.txt_info4 = Label(self.frame_principal2, text='INFO4', bg = self.cor1, fg = self.cor2, font=('arial', 20))
        self.txt_info4.place(relx=0.55, rely=0.1)
        #COMANDO PARA USAR NO BOTÃO

    def mostrar5(self):
        self.limpar()
        self.image5 = PhotoImage(file='images/botao5.png')
        self.imagem5= Label(self.frame_principal2, image = self.image5, bg = self.cor1)
        self.imagem5.place(relx=0.05, rely=0.12)
        self.txt_info5 = Label(self.frame_principal2, text='INFO5', bg = self.cor1, fg = self.cor2, font=('arial', 20))
        self.txt_info5.place(relx=0.55, rely=0.1)
        #COMANDO PARA USAR NO BOTÃO



    def limpar(self):
        for item in self.frame_principal2.winfo_children():
            item.destroy()
        for item in self.frame_principal2.winfo_children():
            item.destroy()

    #LIMPAR CODIGO USAR NO BOTÃO
        
    def sair(self):
        self.root.destroy()

    #SAIR DO PROGRAMA USAR O BOTÃO