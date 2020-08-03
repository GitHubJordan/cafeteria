from tkinter import*
import random
import time;
import datetime


root = Tk()
root.geometry("1350x750+0+0")
root.title("SISTEMA DE VENDAS")
root.configure(background='gray')
root.iconbitmap("ícone.ico")

# ======================== FRAME PRIMARIOS ===========================
Tops = Frame (root, width=1250 , height=1250 , bd=14 , relief="raise")
Tops.pack(side=TOP)

framef1 = Frame (root, width=820 , height=650 , bd=8 , relief="raise")
framef1.pack(side=LEFT)

framef2 = Frame (root, width=440 , height=650 , bd=8 , relief="raise")
framef2.pack(side=RIGHT)

# ======================== FRAME SECUNDARIA ===========================
frameft2 = Frame (framef2, width=440 , height=650 , bd=2 , relief="raise")
frameft2.pack(side=TOP)

framefb2 = Frame (framef2, width=440 , height=250 ,bg='black', bd=2 , relief="raise")
framefb2.pack(side=BOTTOM)

framefla = Frame (framef1, width=900 , height=320 , bd=2 , relief="raise")
framefla.pack(side=TOP)

framef2a = Frame (framef1, width=820 , height=300 , bd=2 , relief="raise")
framef2a.pack(side=BOTTOM)

frameflaa = Frame (framefla, width=450 , height=310 , bd=2 , relief="raise")
frameflaa.pack(side=LEFT)

frameflab = Frame (framefla, width=450 , height=310 , bd=2 , relief="raise")
frameflab.pack(side=RIGHT)

# ======================== CRIANDO FRAMES DO RODAPE ===========================

framef2aa = Frame (framef2a,width=315,height=800,bd=2,relief="raise")
framef2aa.pack(side=LEFT)

framef2ab = Frame (framef2a,width=315,height=800,bd=2,relief="raise")
framef2ab.pack(side=RIGHT)

frameRODAPE = Frame (framef2a,width=210,height=190,bd=2,relief="raise")
frameRODAPE.pack(side=BOTTOM)


# ======================== TROCANDO A COR DO FUNDO DO FRAME DA ESQUERDA ===========================

Tops.configure(background= 'gray')
framef1.configure(background= 'gray')
frameflaa.configure(background= 'DarkSeaGreen3')
frameflab.configure(background= 'DarkSeaGreen3')
framef2a.configure(background= 'Burlywood3')

framef2aa.configure(background= 'Burlywood3')
framef2ab.configure(background= 'Burlywood3')
frameRODAPE.configure(background= 'Burlywood3')
frameft2.configure(background= 'IndianRed3')


# ======================== INSIRINDO O ROTULO DO CABEÇALHO COM O TITULO ===========================

lblInfo= Label(Tops,font=('arial',53,'bold'),text="SISTEMA JAM",bd=25,width=28)
lblInfo.grid(row=0,column=0)

#txtRecibo = Label(frameft2,font=('arial',53,'bold'),text="SISTEMA JAM",bd=25,width=22)
#txtRecibo.grid(row=1,column=0)


# ======================== OUTROS ===========================


# ======================== CREIANDO OS METODOS DOS BOTOES ==============================
# ======================== CREIANDO O CODIGO DO BOTAO RECIBO ===========================

def Recibo():
    pass
    


# ======================== CREIANDO O CODIGO DO BOTAO SAIR ===========================

def iExit():
    root.destroy()
    return

# ======================== CREIANDO O CODIGO DO BOTAO LIMPAR ===========================

def Limpar():
    txtRecibo .delete("1.0",END)
    Imposto .set("")
    Subtotal .set("")
    Total .set("")
    Totalbolo .set("")
    Totalbebida .set("")
    Taxaservico .set("")
    QTBebida .set("")



    C_Latte .set("0")
    C_Espresso .set("0")
    C_Iced_Latte .set("0")
    C_Cafe_Cortado .set("0")
    C_Cafe_Leite .set("0")
    C_Cafe_Preto .set("0")
    C_Cafe_Creme .set("0")
    C_Cappuccion .set("0")

    B_Bolo_Cafe .set("0")
    B_Bolo_Cenoura .set("0")
    B_Bolo_Milho .set("0")
    B_Bolo_Banana .set("0")
    B_Bolo_Morango .set("0")
    B_Bolo_limao .set("0")
    B_Torta .set("0")
    B_Bolo_Chocolate .set("0")

    C_Latte1 .set("")




    

    txtLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtCafe_Cortado.configure(state=DISABLED)
    txtCafe_Leite.configure(state=DISABLED)
    txtCafe_Preto.configure(state=DISABLED)
    txtCafe_Creme.configure(state=DISABLED)
    txtCappuccion.configure(state=DISABLED)

    txtBolo_Cafe.configure(state=DISABLED)
    txtBolo_Cenoura.configure(state=DISABLED)
    txtBolo_Milho.configure(state=DISABLED)
    txtBolo_Banana.configure(state=DISABLED)
    txtBolo_Morango.configure(state=DISABLED)
    txtBolo_limao.configure(state=DISABLED)
    txtTorta.configure(state=DISABLED)
    txtBolo_Chocolate.configure(state=DISABLED)


# ======================== CREIANDO OS METODOS PARA OS RADIO BUTTONS ===========================

def custoItem():
    Item1=float(C_Latte.get())
    Item2=float(C_Espresso.get())
    Item3=float(C_Iced_Latte.get())
    Item4=float(C_Cafe_Cortado.get())
    Item5=float(C_Cafe_Leite.get())
    Item6=float(C_Cafe_Preto.get())
    Item7=float(C_Cafe_Creme.get())
    Item8=float(C_Cappuccion.get())

    Item9=float(B_Bolo_Cafe.get())
    Item10=float(B_Bolo_Cafe.get())
    Item11=float(B_Bolo_Milho.get())
    Item12=float(B_Bolo_Banana.get())
    Item13=float(B_Bolo_Morango.get())
    Item14=float(B_Bolo_limao.get())
    Item15=float(B_Torta.get())
    Item16=float(B_Bolo_Chocolate.get())

    Precobebidas=(Item1 * 100.2)+(Item2 * 100.99)+(Item3 * 200.05)+(Item4 * 200.10)+(Item5 * 100.99)+(Item6 * 200.99)+(Item7 * 100.99)+(Item8 * 100.99)
    Precobolos=(Item9 * 100.2)+(Item10 * 100.99)+(Item11 * 200.05)+(Item12 * 200.10)+(Item13 * 100.99)+(Item14 * 200.99)+(Item15 * 100.99)+(Item16 * 100.99)


    Bebidapreco="AKZ",str('%.2f'%(Precobebidas))
    Bolopreco="AKZ",str('%.2f'%(Precobolos))
    Totalbolo.set(Bolopreco)
    Totalbebida.set(Bebidapreco)
    SC="AKZ",str('%.2f'%(0.10))
    Taxaservico.set(SC)

    SubTotalItens="AKZ",str('%.2f'%(Precobebidas+Precobolos +0.10))
    Subtotal.set(SubTotalItens)

    Taxa="AKZ",str('%.2f'%((Precobebidas + Precobolos +0.10)*0.15))
    Imposto.set(Taxa)

    TT=((Precobebidas + Precobolos +0.10)*0.15)
    TC="AKZ",str('%.2f'%(Precobebidas + Precobolos +1.60 + TT))
    Total.set(TC)


##    lbl1Rcibo10 = Label(frameft2,font=('aria',10),text=txtLatte,bg='lemonchiffon', textvariable=C_Latte,bd=2,fg=None,anchor=None)
##    lbl1Rcibo10.grid(row=1,column=0,sticky=None)
##    lbl1Rcibo10.place(x=177, y=290)        
##    QTBebida.set(lbl1Rcibo10)

##    lbl1Rcibo11 = Label(frameft2,font=('aria',10),text=txtLatte,bg='lemonchiffon', textvariable=C_Espresso,bd=2,fg=None,anchor=None)
##    lbl1Rcibo11.grid(row=1,column=0,sticky=None)
##    lbl1Rcibo11.place(x=177, y=310)        
##    QTBebida.set(lbl1Rcibo11)

##    lbl1Rcibo12 = Label(frameft2,font=('aria',10),text=txtLatte,bg='lemonchiffon', textvariable=orTotal,bd=2,fg=None,anchor=None)
##    lbl1Rcibo12.grid(row=1,column=0,sticky=None)
##    lbl1Rcibo12.place(x=177, y=350)        
##    QTBebida.set(lbl1Rcibo12)

##    ouTotal = (lbl1Rcibo10 + lbl1Rcibo11)
##    orTotal.set(ouTotal)



# ======================== CREIANDO OS METODOS PARA OS RADIO BUTTONS ===========================

def chkLatte():
    if(var1.get()==1):
        txtLatte.configure(state=NORMAL)
        C_Latte.set("")
    elif(var1.get()==0):
        txtLatte.configure(state=DISABLED)
        C_Latte.set("0")

def chkEspresso():
    if(var2.get()==1):
        txtEspresso.configure(state=NORMAL)
        C_Espresso.set("")
    elif(var2.get()==0):
        txtEspresso.configure(state=DISABLED)
        C_Espresso.set("0")

def chkIced_Latte():
    if(var3.get()==1):
        txtIced_Latte.configure(state=NORMAL)
        C_Iced_Latte.set("")
    elif(var3.get()==0):
        txtIced_Latte.configure(state=DISABLED)
        C_Iced_Latte.set("0")

def chkCafe_Cortado():
    if(var4.get()==1):
        txtCafe_Cortado.configure(state=NORMAL)
        C_Cafe_Cortado.set("")
    elif(var4.get()==0):
        txtCafe_Cortado.configure(state=DISABLED)
        C_Cafe_Cortado.set("0")

def chkCafe_Leite():
    if(var5.get()==1):
        txtCafe_Leite.configure(state=NORMAL)
        C_Cafe_Leite.set("")
    elif(var5.get()==0):
        txtCafe_Leite.configure(state=DISABLED)
        C_Cafe_Leite.set("0")

def chkCafe_Preto():
    if(var6.get()==1):
        txtCafe_Preto.configure(state=NORMAL)
        C_Cafe_Preto.set("")
    elif(var6.get()==0):
        txtCafe_Preto.configure(state=DISABLED)
        C_Cafe_Preto.set("0")

def chkCafe_Creme():
    if(var7.get()==1):
        txtCafe_Creme.configure(state=NORMAL)
        C_Cafe_Creme.set("")
    elif(var7.get()==0):
        txtCafe_Creme.configure(state=DISABLED)
        C_Cafe_Creme.set("0")

def chkCappuccion():
    if(var8.get()==1):
        txtCappuccion.configure(state=NORMAL)
        C_Cappuccion.set("")
    elif(var8.get()==0):
        txtCappuccion.configure(state=DISABLED)
        C_Cappuccion.set("0")



def chkBolo_Cafe():
    if(var9.get()==1):
        txtBolo_Cafe.configure(state=NORMAL)
        B_Bolo_Cafe.set("")
    elif(var9.get()==0):
        txtBolo_Cafe.configure(state=DISABLED)
        B_Bolo_Cafe.set("0")

def chkBolo_Cenoura():
    if(var10.get()==1):
        txtBolo_Cenoura.configure(state=NORMAL)
        B_Bolo_Cenoura.set("")
    elif(var1.get()==0):
        txtBolo_Cenoura.configure(state=DISABLED)
        B_Bolo_Cenoura.set("0")

def chkBolo_Milho():
    if(var11.get()==1):
        txtBolo_Milho.configure(state=NORMAL)
        B_Bolo_Milho.set("")
    elif(var11.get()==0):
        txtBolo_Milho.configure(state=DISABLED)
        B_Bolo_Milho.set("0")

def chkBolo_Banana():
    if(var12.get()==1):
        txtBolo_Banana.configure(state=NORMAL)
        B_Bolo_Banana.set("")
    elif(var12.get()==0):
        txtBolo_Banana.configure(state=DISABLED)
        B_Bolo_Banana.set("0")

def chkBolo_Morango():
    if(var13.get()==1):
        txtBolo_Morango.configure(state=NORMAL)
        B_Bolo_Morango.set("")
    elif(var13.get()==0):
        txtBolo_Morango.configure(state=DISABLED)
        B_Bolo_Morango.set("0")

def chkBolo_limao():
    if(var14.get()==1):
        txtBolo_limao.configure(state=NORMAL)
        B_Bolo_limao.set("")
    elif(var1.get()==0):
        txtBolo_limao.configure(state=DISABLED)
        B_Bolo_limao.set("0")

def chkTorta():
    if(var15.get()==1):
        txtTorta.configure(state=NORMAL)
        B_Torta.set("")
    elif(var15.get()==0):
        txtTorta.configure(state=DISABLED)
        B_Torta.set("0")

def chkBolo_Chocolate():
    if(var16.get()==1):
        txtBolo_Chocolate.configure(state=NORMAL)
        B_Bolo_Chocolate.set("")
    elif(var16.get()==0):
        txtBolo_Chocolate.configure(state=DISABLED)
        B_Bolo_Chocolate.set("0")







# ==================== DECLARANDO AS PRIMEIRAS VARIAVEIS =======================
C_Latte =StringVar()
C_Espresso =StringVar()
C_Iced_Latte =StringVar()
C_Cafe_Cortado =StringVar()
C_Cafe_Leite =StringVar()
C_Cafe_Preto =StringVar()
C_Cafe_Creme =StringVar()
C_Cappuccion =StringVar()


B_Bolo_Cafe =StringVar()
B_Bolo_Cenoura =StringVar()
B_Bolo_Milho =StringVar()
B_Bolo_Banana =StringVar()
B_Bolo_Morango =StringVar()
B_Bolo_limao =StringVar()
B_Torta =StringVar()
B_Bolo_Chocolate =StringVar()

C_Latte1 =StringVar()




# ====================  VARIAVEIS DO RODAPE ====================================

Dataordem =StringVar()
Recibo =StringVar()
Imposto =StringVar()
Subtotal =StringVar()
Total =StringVar()
Totalbolo =StringVar()
Totalbebida =StringVar()
Taxaservico =StringVar()
QTBebida =StringVar()
orTotal =StringVar ()




var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

var17= IntVar()


# ==================== SITANDO AS VARIAVEIS =======================
C_Latte .set("0")
C_Espresso .set("0")
C_Iced_Latte .set("0")
C_Cafe_Cortado .set("0")
C_Cafe_Leite .set("0")
C_Cafe_Preto .set("0")
C_Cafe_Creme .set("0")
C_Cappuccion .set("0")

B_Bolo_Cafe .set("0")
B_Bolo_Cenoura .set("0")
B_Bolo_Milho .set("0")
B_Bolo_Banana .set("0")
B_Bolo_Morango .set("0")
B_Bolo_limao .set("0")
B_Torta .set("0")
B_Bolo_Chocolate .set("0")

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")

C_Latte1 .set("0")
var17.set("0")



# =========================== CRIANDO OS RADIO BUTTONS PARA OS CAFES ==============================

Latte= Checkbutton(frameflaa,text="Latte \t",variable = var1,onvalue =1, offvalue=0,width=9,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkLatte).grid(row = 0,sticky=W)
Espresso= Checkbutton(frameflaa,text="Espresso \t",variable = var2,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkEspresso).grid(row = 1,sticky=W)
Iced_Latte= Checkbutton(frameflaa,text="Iced_Latte \t",variable = var3,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkIced_Latte).grid(row = 2,sticky=W)
Cafe_Cortado= Checkbutton(frameflaa,text="Cafe_Cortado \t",variable = var4,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkCafe_Cortado).grid(row = 3,sticky=W)
Cafe_Leite= Checkbutton(frameflaa,text="Cafe_Leite \t",variable = var5,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkCafe_Leite).grid(row = 4,sticky=W)
Cafe_Preto= Checkbutton(frameflaa,text="Cafe_Preto \t",variable = var6,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkCafe_Preto).grid(row = 5,sticky=W)
Cafe_Creme= Checkbutton(frameflaa,text="Cafe_Creme \t",variable = var7,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkCafe_Creme).grid(row = 6,sticky=W)
Cappuccion= Checkbutton(frameflaa,text="Cappuccion \t",variable = var8,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkCappuccion).grid(row = 7,sticky=W)

# =========================== CRIANDO OS RADIO BUTTONS PARA OS BOLOS ==============================

Bolo_Cafe= Checkbutton(frameflab,text="Bolo_Cafe \t",variable = var9,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Cafe).grid(row = 0,sticky=W)
Bolo_Cenoura= Checkbutton(frameflab,text="Bolo_Cenoura \t",variable = var10,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Cenoura).grid(row = 1,sticky=W)
Bolo_Milho= Checkbutton(frameflab,text="Bolo_Milho \t",variable = var11,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Milho).grid(row = 2,sticky=W)
Bolo_Banana= Checkbutton(frameflab,text="Bolo_Banana \t",variable = var12,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Banana).grid(row = 3,sticky=W)
Bolo_Morango= Checkbutton(frameflab,text="Bolo_Morango \t",variable = var13,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Morango).grid(row = 4,sticky=W)
Bolo_limao= Checkbutton(frameflab,text="Bolo_limao \t",variable = var14,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_limao).grid(row = 5,sticky=W)
Torta= Checkbutton(frameflab,text="Torta \t",variable = var15,onvalue =1, offvalue=0,width=9,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkTorta).grid(row = 6,sticky=W)
Bolo_Chocolate= Checkbutton(frameflab,text="Bolo_Chocolate \t",variable = var16,onvalue =1, offvalue=0,width=16,bg='DarkSeaGreen3',fg='blue',
                   font=('arial',18,'bold'),command=chkBolo_Chocolate).grid(row = 7,sticky=W)



# =========================== CRIANDO OS CAMPOS DE TEXTO, CAIXA DE TEXTO. ==============================

txtLatte=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Latte,state=DISABLED)
txtLatte.grid(row=0,column=1)

txtEspresso=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Espresso,state=DISABLED)
txtEspresso.grid(row=1,column=1)

txtIced_Latte=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Iced_Latte,state=DISABLED)
txtIced_Latte.grid(row=2,column=1)

txtCafe_Cortado=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Cafe_Cortado,state=DISABLED)
txtCafe_Cortado.grid(row=3,column=1)

txtCafe_Leite=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Cafe_Leite,state=DISABLED)
txtCafe_Leite.grid(row=4,column=1)

txtCafe_Preto=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Cafe_Preto,state=DISABLED)
txtCafe_Preto.grid(row=5,column=1)

txtCafe_Creme=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Cafe_Creme,state=DISABLED)
txtCafe_Creme.grid(row=6,column=1)

txtCappuccion=Entry (frameflaa,font=('arial',18,'bold'),bd=2,bg='SkyBlue',width=6,justify='left',textvariable=C_Cappuccion,state=DISABLED)
txtCappuccion.grid(row=7,column=1)



txtBolo_Cafe=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Cafe,state=DISABLED)
txtBolo_Cafe.grid(row=0,column=1)

txtBolo_Cenoura=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Cenoura,state=DISABLED)
txtBolo_Cenoura.grid(row=1,column=1)

txtBolo_Milho=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Milho,state=DISABLED)
txtBolo_Milho.grid(row=2,column=1)

txtBolo_Banana=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Banana,state=DISABLED)
txtBolo_Banana.grid(row=3,column=1)

txtBolo_Morango=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Morango,state=DISABLED)
txtBolo_Morango.grid(row=4,column=1)

txtBolo_limao=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_limao,state=DISABLED)
txtBolo_limao.grid(row=5,column=1)

txtTorta=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Torta,state=DISABLED)
txtTorta.grid(row=6,column=1)

txtBolo_Chocolate=Entry (frameflab,font=('arial',18,'bold'),bd=2,width=6,justify='left',textvariable=B_Bolo_Chocolate,state=DISABLED)
txtBolo_Chocolate.grid(row=7,column=1)




# ================================================== CAMPO DO RECIBO =====================================================


lblRecibo = Label(frameft2,font=('aria',12,'bold'),text="Recibo do Cliente",bg='IndianRed3',bd=2,fg='white',width=50,anchor='w')
lblRecibo.grid(row=0,column=0,sticky=W)

txtRecibo = Text(frameft2,width=70,height=43,bg="lemonchiffon",bd=8,font=('arial',10),state=DISABLED)
txtRecibo.grid(row=1,column=0)


##==================================================outros=======================================================================
lblRcibo1 = Label(frameft2,font=('aria',10),text="  Recibo do Cliente",bg='lemonchiffon',bd=2,fg=None,anchor=None)
lblRcibo1.grid(row=1,column=0,sticky=None)
lblRcibo1.place(x=140, y=45)


##==================================================outros=======================================================================

##
##
##

##==================================================outros=======================================================================

##lblRcibo2 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=QTBebida,fg=None,anchor=None)
##lblRcibo2.grid(row=1,column=0,sticky=None)
##lblRcibo2.place(x=177, y=350)

lblRcibo2 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Totalbebida,fg=None,anchor=None)
lblRcibo2.grid(row=1,column=0,sticky=None)
lblRcibo2.place(x=177, y=80)

lblRcibo3 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Totalbolo,fg=None,anchor=None)
lblRcibo3.grid(row=1,column=0,sticky=None)
lblRcibo3.place(x=177, y=110)

lblRcibo4 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Taxaservico,fg=None,anchor=None)
lblRcibo4.grid(row=1,column=0,sticky=None)
lblRcibo4.place(x=177, y=140)

lblRcibo5 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Imposto,fg=None,anchor=None)
lblRcibo5.grid(row=1,column=0,sticky=None)
lblRcibo5.place(x=177, y=170)

lblRcibo6 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Subtotal,fg=None,anchor=None)
lblRcibo6.grid(row=1,column=0,sticky=None)
lblRcibo6.place(x=177, y=200)

lblRcibo7 = Label(frameft2,font=('aria',10),text="AngoMart",bg='lemonchiffon',bd=2, textvariable=Total,fg=None,anchor=None)
lblRcibo7.grid(row=1,column=0,sticky=None)
lblRcibo7.place(x=177, y=230)

##==================================================outros======================================================================
lblCustobebidas = Label(frameft2,font=('arial',10),text="Custo Bebidas:",bd=2,bg='lemonchiffon')
lblCustobebidas.grid(row=0,column=0,sticky=None)
lblCustobebidas.place(x=50, y=80)

lblCustobolos = Label(frameft2,font=('arial',10,),text="Custo Bolos:",bd=2,bg='lemonchiffon')
lblCustobolos.grid(row=0,column=0,sticky=None)
lblCustobolos.place(x=50, y=110)


lblTaxaservicos = Label(frameft2,font=('arial',10,),text="Taxa Servicos:",bd=2,bg='lemonchiffon')
lblTaxaservicos.grid(row=0,column=0,sticky=None)
lblTaxaservicos.place(x=50, y=140)


lblImposto = Label(frameft2,font=('arial',10,),text="Imposto:",bd=2,bg='lemonchiffon')
lblImposto.grid(row=0,column=0,sticky=None)
lblImposto.place(x=50, y=170)


lblSubtotal = Label(frameft2,font=('arial',10,),text="Sub Total:",bd=2,bg='lemonchiffon')
lblSubtotal.grid(row=0,column=0,sticky=None)
lblSubtotal.place(x=50, y=200)


lblTotal = Label(frameft2,font=('arial',10,),text="Total:",bd=2,bg='lemonchiffon')
lblTotal.grid(row=0,column=0,sticky=None)
lblTotal.place(x=50, y=230)



# =========================== CAMPO DE BOTOES ==========================================================

cmdTotal=Button(framefb2,padx=16,pady=1,bg='black',bd=4,fg='green',font=('arial',12,'bold'),width=9,
                text="Total",command=custoItem).grid(row=0,column=0)
cmdRecibo=Button(framefb2,padx=16,pady=1,bg='black',bd=4,fg='white',font=('arial',12,'bold'),width=8,
                text="Recibo",command=Recibo).grid(row=0,column=1)
cmdLimpar=Button(framefb2,padx=16,pady=1,bg='black',bd=4,fg='yellow',font=('arial',12,'bold'),width=8,
                text="Limpar",command=Limpar).grid(row=0,column=2)
cmdSair=Button(framefb2,padx=16,pady=1,bg='black',bd=5,fg='red',font=('arial',12,'bold'),width=8,
                text="Sair",command=iExit).grid(row=0,column=3)


# =========================== CRIANDO OS CAMPOS DO RODAPE FRAME DA ESQUERDA ==============================

lblCustobebidas = Label(framef2aa,font=('arial',12,'bold'),text=" ",bd=2,bg='Burlywood3',height=3)
lblCustobebidas.grid(row=0,column=0,sticky=W)



lblCustobebidas = Label(framef2aa,font=('arial',12,'bold'),text="Custo Bebidas:",bd=2,bg='Burlywood3',height=1)
lblCustobebidas.grid(row=1,column=0,sticky=W)

lblCustobebidas = Entry(framef2aa,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Totalbebida)
lblCustobebidas.grid(row=1,column=1)


lblCustobolos = Label(framef2aa,font=('arial',12,'bold'),text="Custo Bolos:",bd=2,bg='Burlywood3',height=1)
lblCustobolos.grid(row=2,column=0,sticky=W)

lblCustobolos = Entry(framef2aa,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Totalbolo)
lblCustobolos.grid(row=2,column=1)


lblTaxaservicos = Label(framef2aa,font=('arial',12,'bold'),text="Taxa Servicos:",bd=2,bg='Burlywood3',height=1)
lblTaxaservicos.grid(row=3,column=0,sticky=W)

lblTaxaservicos = Entry(framef2aa,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Taxaservico)
lblTaxaservicos.grid(row=3,column=1)


lblCustobebidas = Label(framef2aa,font=('arial',12,'bold'),text=" ",bd=2,bg='Burlywood3',height=3)
lblCustobebidas.grid(row=4,column=0,sticky=W)




# =========================== CRIANDO OS CAMPOS DO RODAPE FRAME DA DIREITA ==============================

lblImposto = Label(framef2ab,font=('arial',12,'bold'),text=" ",bd=2,bg='Burlywood3',height=3)
lblImposto.grid(row=0,column=0,sticky=W)


lblImposto = Label(framef2ab,font=('arial',12,'bold'),text="Imposto:",bd=2,bg='Burlywood3',height=1)
lblImposto.grid(row=1,column=0,sticky=W)

lblImposto = Entry(framef2ab,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Imposto)
lblImposto.grid(row=1,column=1)


lblSubtotal = Label(framef2ab,font=('arial',12,'bold'),text="Sub Total:",bd=2,bg='Burlywood3',height=1)
lblSubtotal.grid(row=2,column=0,sticky=W)

lblSubtotal = Entry(framef2ab,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Subtotal)
lblSubtotal.grid(row=2,column=1)


lblTotal = Label(framef2ab,font=('arial',12,'bold'),text="Total:",bd=2,bg='Burlywood3',height=1)
lblTotal.grid(row=3,column=0,sticky=W)

lblTotal = Entry(framef2ab,font=('arial',10,'bold'),bd=2,justify='left',textvariable=Total)
lblTotal.grid(row=3,column=1)


lblImposto = Label(framef2ab,font=('arial',12,'bold'),text=" ",bd=2,bg='Burlywood3',height=3)
lblImposto.grid(row=4,column=0,sticky=W)


root.mainloop()
