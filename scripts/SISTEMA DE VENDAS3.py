from tkinter import*
import random
import time;
import datetime


root = Tk()
root.geometry("1350x750+0+0")
root.title("SISTEMA DE VENDAS")
root.configure(background='blue')

# ======================== FRAME PRIMARIOS ===========================
Tops = Frame (root, width=1250 , height=100 , bd=14 , relief="raise")
Tops.pack(side=TOP)

framef1 = Frame (root, width=820 , height=650 , bd=8 , relief="raise")
framef1.pack(side=LEFT)

framef2 = Frame (root, width=440 , height=650 , bd=8 , relief="raise")
framef2.pack(side=RIGHT)

# ======================== FRAME SECUNDARIA ===========================
frameft2 = Frame (framef2, width=440 , height=650 , bd=2 , relief="raise")
frameft2.pack(side=TOP)

framefb2 = Frame (framef2, width=440 , height=50 , bd=2 , relief="raise")
framefb2.pack(side=BOTTOM)

framefla = Frame (framef1, width=900 , height=320 , bd=2 , relief="raise")
framefla.pack(side=TOP)

framef2a = Frame (framef1, width=820 , height=300 , bd=2 , relief="raise")
framef2a.pack(side=BOTTOM)

frameflaa = Frame (framefla, width=450 , height=310 , bd=2 , relief="raise")
frameflaa.pack(side=LEFT)

frameflab = Frame (framefla, width=450 , height=310 , bd=2 , relief="raise")
frameflab.pack(side=RIGHT)




# ======================== TROCANDO A COR DO FUNDO DO FRAME DA ESQUERDA ===========================

framef1.configure(background= 'gray')

# ======================== INSIRINDO O ROTULO DO CABEÇALHO COM O TITULO ===========================

lblInfo= Label(Tops,font=('arial',50,'bold'),text="SISTEMA JAM",bd=20,width=24)
lblInfo.grid(row=0,column=0)



# ==================== DECLARANDO AS PRIMEIRAS VARIAVEIS =======================

var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()

var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()
var17= IntVar()

# ==================== SITANDO AS VARIAVEIS =======================

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")

var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")


# =========================== CRIANDO OS RADIO BUTTONS PARA OS CAFES ==============================

Latte= Checkbutton(frameflaa,text="Latte \t",variable = var1,onvalue =1, offvalue=0,width=8,
                   font=('arial',18,'bold')).grid(row = 0,sticky=W)
Espresso= Checkbutton(frameflaa,text="Espresso \t",variable = var2,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 1,sticky=W)
Iced_Latte= Checkbutton(frameflaa,text="Iced_Latte \t",variable = var3,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 2,sticky=W)
Cafe_Cortado= Checkbutton(frameflaa,text="Cafe_Cortado \t",variable = var4,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 3,sticky=W)
Cafe_Leite= Checkbutton(frameflaa,text="Cafe_Leite \t",variable = var5,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 4,sticky=W)
Cafe_Preto= Checkbutton(frameflaa,text="Cafe_Preto \t",variable = var6,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 5,sticky=W)
Cafe_Creme= Checkbutton(frameflaa,text="Cafe_Creme \t",variable = var7,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 6,sticky=W)
Cappuccion= Checkbutton(frameflaa,text="Cappuccion \t",variable = var8,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 7,sticky=W)

# =========================== CRIANDO OS RADIO BUTTONS PARA OS BOLOS ==============================

Bolo_Cafe= Checkbutton(frameflab,text="Bolo_Cafe \t",variable = var10,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 0,sticky=W)
Bolo_Cenoura= Checkbutton(frameflab,text="Bolo_Cenoura \t",variable = var11,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 1,sticky=W)
Bolo_Milho= Checkbutton(frameflab,text="Bolo_Milho \t",variable = var12,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 2,sticky=W)
Bolo_Banana= Checkbutton(frameflab,text="Bolo_Banana \t",variable = var13,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 3,sticky=W)
Bolo_Morango= Checkbutton(frameflab,text="Bolo_Morango \t",variable = var14,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 4,sticky=W)
Bolo_limao= Checkbutton(frameflab,text="Bolo_limao \t",variable = var15,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 5,sticky=W)
Torta= Checkbutton(frameflab,text="Torta \t",variable = var16,onvalue =1, offvalue=0,width=8,
                   font=('arial',18,'bold')).grid(row = 6,sticky=W)
Bolo_Chocolate= Checkbutton(frameflab,text="Bolo_Chocolate \t",variable = var17,onvalue =1, offvalue=0,width=16,
                   font=('arial',18,'bold')).grid(row = 7,sticky=W)

# =========================== CRIANDO OS CAMPOS DE TEXTO, CAIXA DE TEXTO. ==============================

txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=0,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=1,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=2,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=3,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=4,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=5,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=6,column=1)
txtLatte=Entry (frameflaa,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=7,column=1)


txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=0,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=1,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=2,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=3,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=4,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=5,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=6,column=1)
txtLatte=Entry (frameflab,font=('arial',16,'bold'),bd=1,width=7,justify='left',state=DISABLED)
txtLatte.grid(row=7,column=1)

# =========================== CAMPO DO RECIBO ==============================

lblRecibo = Label(frameft2,font=('aria',12,'bold'),text="Recibo do Cliente",bd=2,anchor='w')
lblRecibo.grid(row=0,column=0,sticky=W)

txtRecibo = Text(frameft2,width=59,height=25,bg="lemonchiffon",bd=8,font=('arial',10))
txtRecibo.grid(row=1,column=0)

# =========================== CAMPO DE BOTOES ==============================

cmdTotal=Button(framefb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,
                text="Total").grid(row=0,column=0)
cmdRecibo=Button(framefb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,
                text="Recibo").grid(row=0,column=1)
cmdLimpar=Button(framefb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,
                text="Limpar").grid(row=0,column=2)
cmdSair=Button(framefb2,padx=16,pady=1,bd=4,fg='black',font=('arial',12,'bold'),width=5,
                text="Sair").grid(row=0,column=3)




root.mainloop()
