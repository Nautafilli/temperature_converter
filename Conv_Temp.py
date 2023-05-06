from tkinter import *

mw = Tk()
mw.title("Conversion de temperatura")

#-------------------------------------------------- declaracion de variables
mw_w = 435
mw_h =190
temp = StringVar()

#-------------------------------------------------- dimensionamiento y centrado automatico de la pantalla
mw.geometry(str(int(mw_w) ) + "x" + str(int(mw_h))  + "+" + str(int(mw.winfo_screenwidth()/2)-int(mw_w/2)) + "+" + str(int(mw.winfo_screenheight()/2)-int(mw_h/2)))

#-------------------------------------------------- definciones
def c2f():
    l4["text"]=str(float(temp.get())*9/5+32)
    l2["text"]='\N{DEGREE SIGN}'+"C"
    l5["text"]='\N{DEGREE SIGN}'+"F"
    b1["bg"]="light gray"
    b2["bg"]="#f0f0f0"

def f2c():
    l4["text"]=str((float(temp.get())-32)*5/9)
    l2["text"]='\N{DEGREE SIGN}'+"F"
    l5["text"]='\N{DEGREE SIGN}'+"C"
    b2["bg"]="lightgray"
    b1["bg"]="#f0f0f0"


#-------------------------------------------------- Programa principal
    
#Row 0
l1 = Label(mw, text="Temperatura a convertir: ", font="arial 12", height=2).grid(column=0, row=0)
e1 = Entry(mw, textvariable=temp, relief="groove",font="arial 12").grid(column=1, row=0)
l2 = Label(mw, text=" -- ", font="arial 10")
l2.grid(column = 2, row=0)
#Row 1
b1 = Button(mw, text = '\N{DEGREE SIGN}' +"C  --> " + '\N{DEGREE SIGN}' + "F", command=c2f, width=25, height=2)
b1.grid(column=0, row=1)
b2 = Button(mw, text = '\N{DEGREE SIGN}' + "F  --> " + '\N{DEGREE SIGN}' + "C", command=f2c, width=25, height=2)
b2.grid(column=1, row=1)
#Row 2
l3 = Label(mw, text="Temperatura a convertida: ", font="arial 12").grid(column=0, row=2, padx=5, pady=5)
l4 = Label(mw, text=" -- ", font="arial 12", width=15, height=2, relief="groove")
l4.grid(column = 1, row=2, padx=5, pady=5)
l5 = Label(mw, text=" -- ", font="arial 10")
l5.grid(column = 2, row=2)
#Row 3
b3 = Button(mw, text="Salir", command=mw.destroy, bg="red", font="arial 12", width=45).grid(column=0, row=3, columnspan=3, ipadx=5, ipady=5, padx=5, pady=10)

print(temp.get())

mw.mainloop()