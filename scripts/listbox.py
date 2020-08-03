from tkinter import*
import tkinter.ttk as ttk

form = Tk()
form.title("LISTBOX")


#DEFININDO O TAMANHO DO FORMULARIO

width = 450
height = 300
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()
x= (screen_width/2)-(width/2)
y= (screen_height/2)-(height/2)

form.geometry("%dx%d+%d+%d" % (width,height,x,y))
form.resizable(0,0)
form.configure(bg="lightSteelBlue3")

#CRIANDO METODO INSERIR DADOS NA LISTBOX
def Inserirdados():
    listbox.insert(END,inserir.get())

def Removerdados():
	pass

def Fechar():
	form.destroy()
	

#CRIANDO LABEL DA LISTBOX
lbllistbox= Label(form,text="LISTBOX from JAM",bg="lightSteelBlue3",fg='blue',font=('Times New Roman',12,'bold')).place(x=50,y=50)

#CRIANDO LISTBOX
listbox= Listbox(form,width=40)
##listbox.insert(0,"LISTBOX 1")
##listbox.insert(1,"LISTBOX 2")
##listbox.insert(2,"LISTBOX 3")
##listbox.insert(3,"LISTBOX 4")

listbox.place(x=50,y=75)

lbllistbox1= Label(form,text="INSIRINDO DADOS",bg="lightSteelBlue3",fg='blue').place(x=8,y=10)
inserir= StringVar()
txtlistbox= Entry(form,textvariable= inserir,width=36).place(x=140,y=10)
btninserir= Button(form,text="INSERIR",height=1,width=10,  font=('arial',9,'bold'),
					command=Inserirdados).place(x=365,y=7.5)
btnfechar = Button(form, text = "Fechar", height = 1, width = 10, fg='red', font=('arial',9,'bold'),
					command = Fechar).place(x = 365, y = 260)

form.mainloop()
