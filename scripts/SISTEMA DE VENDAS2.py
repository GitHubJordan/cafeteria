from tkinter import*
import random
import time;
import datetime


root = Tk()
root.geometry("1250x750+0+0")
root.title("SISTEMA DE VENDAS")
root.configure(background='blue')

# ======================== FRAME PRIMARIOS ===========================
Tops = Frame (root, width=1250 , height=100 , bd=14 , relief="raise")
Tops.pack(side=TOP)

framef1 = Frame (root, width=820 , height=650 , bd=8 , relief="raise")
framef1.pack(side=LEFT)

framef2 = Frame (root, width=420 , height=650 , bd=8 , relief="raise")
framef2.pack(side=RIGHT)


# ======================== FRAME SECUNDARIA ===========================

frameft2 = Frame (frameft2, width=420 , height=650 , bd=2 , relief="raise")
frameft2.pack(side=TOP)

framefb2 = Frame (framefb2, width=420 , height=50 , bd=2 , relief="raise")
framefb2.pack(side=BOTTOM)

framefla = Frame (framefla, width=850 , height=320 , bd=2 , relief="raise")
framefla.pack(side=TOP)

framef2a = Frame (framef2a, width=850 , height=300 , bd=2 , relief="raise")
framef2a.pack(side=BOTTOM)

frameflaa = Frame (frameflaa, width=320 , height=310 , bd=2 , relief="raise")
frameflaa.pack(side=LEFT)

frameflab = Frame (frameflab, width=320 , height=310 , bd=2 , relief="raise")
frameflab.pack(side=RIGHT)







# ======================== TROCANDO A COR DO FUNDO DO FRAME DA ESQUERDA ===========================

framef1.configure(background= 'gray')

# ======================== INSIRINDO O ROTULO DO CABEÇALHO COM O TITULO ===========================

lblInfo= Label(Tops,font=('arial',50,'bold'),text="SISTEMA JAM",bd=8,width=24)
lblInfo.grid(row=0,column=0)



# ==================== DECLARANDO AS PRIMEIRAS VARIAVEIS =======================


root.mainloop()
