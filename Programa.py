from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import Banco
import Api

def formatcnpj(cnpj):
    return "%s.%s.%s/%s-%s" % ( cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14] )

######################janela 2##########################

def listar_cnpj():

    def popular():
        tv.delete(*tv.get_children())
        vquery="SELECT * FROM Clientes order by CNPJ"
        linhas=Banco.dql(vquery)
        for i in linhas:
            tv.insert("","end",values=i)

    def inserir():
        if vcnpj.get()=="" or vrazao_social.get()=="":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
            return
        try:
            vquery="INSERT INTO Clientes (CNPJ, RAZAO_SOCIAL, SITE) VALUES ('"+vcnpj.get()+"','"+vrazao_social.get()+"','"+vsite.get()+"')"
            Banco.dml(vquery)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao inserir")
            return "%s.%s.%s/%s-%s" % ( cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14] )
        popular()
        vcnpj.delete(0,END)
        vrazao_social.delete(0, END)
        vsite.delete(0, END)
        vcnpj.focus()

    def deletar():
        vcnpj=-1
        itemSelecionado=tv.selection()[0]
        valores=tv.item(itemSelecionado,"values")
        vid=valores[0]
        try:
            vquery="DELETE FROM Clientes WHERE cnpj="+vid
            Banco.dml(vquery)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao deletar")
            return
        tv.delete(itemSelecionado)

    def pesquisar():
        tv.delete(*tv.get_children())

        # cleaning the cnpj
        vcnpj = vcnpjpesquisar.get()
        vcnpj = vcnpj.replace("-", "")
        vcnpj = vcnpj.replace(".", "")
        vcnpj = vcnpj.replace("/", "")


        formato = formatcnpj(vcnpj)

        vquery="SELECT * FROM Clientes WHERE CNPJ LIKE '%"+ formato +"%'"
        linhas=Banco.dql(vquery)
        for i in linhas:
            tv.insert("","end", values=i)

    app=tk.Toplevel(janela1)
    app.title("Listar CNPJs cadastrados")
    app.geometry("700x450")

    quadroGrid=LabelFrame(app, text="Clientes Cadastrados")
    quadroGrid.pack(fill="both", expand="yes", padx=10,pady=10)

    tv=ttk.Treeview(quadroGrid, columns=('cnpj', 'razao_social', 'site'), show='headings')
    tv.column('cnpj',minwidth=0, width=150)
    tv.column('razao_social',minwidth=0, width=250)
    tv.column('site',minwidth=0, width=150)
    tv.heading('cnpj',text='CNPJ')
    tv.heading('razao_social',text='RAZAO_SOCIAL')
    tv.heading('site',text='SITE')
    tv.pack()
    popular()


    #quadroInserir=LabelFrame(app,text="Inserir novo Cliente")
    #quadroInserir.pack(fill="both",expand="yes",padx=10,pady=10)

    #Ibcnpj=Label(quadroInserir,text="CNPJ")
    #Ibcnpj.pack(side="left")
    #vcnpj=Entry(quadroInserir)
    #vcnpj.pack(side="left",padx=8)
    #Ibrazao_social=Label(quadroInserir,text="RAZAO_SOCIAL")
    #Ibrazao_social.pack(side="left")
    #vrazao_social=Entry(quadroInserir)
    #vrazao_social.pack(side="left",padx=8)
    #Ibsite=Label(quadroInserir,text="SITE")
    #Ibsite.pack(side="left")
    #vsite=Entry(quadroInserir)
    #vsite.pack(side="left",padx=8)
    #btn_inserir=Button(quadroInserir, text="Inserir",command=inserir)
    #btn_inserir.pack(side="left",padx=8)

    #####################
    quadroPesquisar=LabelFrame(app,text="Pesquisar Cliente")
    quadroPesquisar.pack(fill="both",expand="yes",padx=10,pady=10)

    Ibcnpj=Label(quadroPesquisar,text="CNPJ")
    Ibcnpj.pack(side="left")
    vcnpjpesquisar=Entry(quadroPesquisar)
    vcnpjpesquisar.pack(side="left",padx=10)

    btn_pesquisar=Button(quadroPesquisar, text="Pesquisar",command=pesquisar)
    btn_pesquisar.pack(side="left",padx=10)

    btn_todos=Button(quadroPesquisar, text="Mostrar Todos",command=popular)
    btn_todos.pack(side="left",padx=10)

###########fim janela2#############

 ####################################janela 3########################
def importar_cnpj():
    janela3 = tk.Toplevel(janela1)
    janela3.title("Importar dados de CNPJ")
    janela3.geometry("700x150")

    def pergunta():
        resultado = messagebox.askquestion(title='Cadastro', message='Deseja criar novo cliente?')
        return resultado


    def inserirRWS():


            if vcnpjRWS.get() == "" or vrazao_socialRWS.get() == "":
                messagebox.showinfo(title="ERRO", message="Digite todos os dados")
                #janela3.destroy()
                return janela1

            else:
                resultsim = pergunta()

                if resultsim == "not":
                    return
                try:
                    vquery = "INSERT INTO Clientes (CNPJ, RAZAO_SOCIAL, SITE) VALUES ('" + vcnpjRWS.get() + "','" + vrazao_socialRWS.get() + "','" + vsiteRWS.get() + "')"
                    Banco.dml(vquery)
                except:
                    messagebox.showinfo(title="ERRO", message="Erro ao inserir")
                    return

            vcnpjRWS.delete(0, END)
            vrazao_socialRWS.delete(0, END)
            vsiteRWS.delete(0, END)
            vcnpjRWS.focus()

            janela3.destroy()


    def pesquisarRWS():
        vcnpjRWS.delete(0, END)
        vrazao_socialRWS.delete(0, END)
        vsiteRWS.delete(0, END)
        vcnpjRWS.focus()

        vcnpj = vcnpjpesquisarRWS.get()

        # cleaning the cnpj
        vcnpj = vcnpj.replace("-", "")
        vcnpj = vcnpj.replace(".", "")
        vcnpj = vcnpj.replace("/", "")

        result = Api.buscar_dados(vcnpj)

        resultado1 = (result['cnpj'])
        resultado2 = (result['nome'])
        resultado3 = (result['email'])

        vcnpjRWS.insert(0,resultado1)
        vrazao_socialRWS.insert(0,resultado2)
        vsiteRWS.insert(0,resultado3)

    def sairrws():
        resultado = messagebox.askquestion(title= 'Sair', message='Deseja realmente sair?')
        if resultado == 'yes':
            janela3.destroy()
            return janela1

    quadroInserirRWS = LabelFrame(janela3, text="Inserir novo Cliente")
    quadroInserirRWS.pack(fill="both", expand="yes", padx=10, pady=10)

    IbcnpjRWS = Label(quadroInserirRWS, text="CNPJ")
    IbcnpjRWS.pack(side="left")
    vcnpjRWS = Entry(quadroInserirRWS)
    vcnpjRWS.pack(side="left", padx=8)
    Ibrazao_socialRWS = Label(quadroInserirRWS, text="RAZAO_SOCIAL")
    Ibrazao_socialRWS.pack(side="left")
    vrazao_socialRWS = Entry(quadroInserirRWS)
    vrazao_socialRWS.pack(side="left", padx=8)
    IbsiteRWS = Label(quadroInserirRWS, text="SITE")
    IbsiteRWS.pack(side="left")
    vsiteRWS = Entry(quadroInserirRWS)
    vsiteRWS.pack(side="left", padx=8)
    btn_inserirRWS = Button(quadroInserirRWS, text="Inserir", command=inserirRWS)
    btn_inserirRWS.pack(side="left", padx=8)

#######################################

    quadroPesquisarRWS = LabelFrame(janela3, text="Pesquisar CNPJ")
    quadroPesquisarRWS.pack(fill="both", expand="yes", padx=10, pady=10)

    IbcnpjRWS = Label(quadroPesquisarRWS, text="CNPJ")
    IbcnpjRWS.pack(side="left")
    vcnpjpesquisarRWS = Entry(quadroPesquisarRWS)
    vcnpjpesquisarRWS.pack(side="left", padx=10)

    btn_pesquisarRWS = Button(quadroPesquisarRWS, text="Pesquisar", command=pesquisarRWS)
    btn_pesquisarRWS.pack(side="left", padx=10)

    btn_sairrws = Button(quadroPesquisarRWS, text="Sair", command=sairrws)
    btn_sairrws.pack(side="left", padx=10)


#########################fim 3###################################

janela1 = tk.Tk()
janela1.title("Cadastro de CNPJ")
janela1.geometry("400x150")

botao2 = tk.Button(janela1,
                   text="Listar CNPJs Cadastrados",
                   command=listar_cnpj)


botao3 = tk.Button(janela1,
                   text="Importar dados de CNPJ",
                   command=importar_cnpj)

botao2.pack()
botao3.pack()

janela1.mainloop()