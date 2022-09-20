from tkinter import *
import re
import random

class App():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("600x400")
        self.raiz.resizable(width=False, height=False)
        self.raiz.title("Expresiones regulares")
        label = Label(self.raiz, text="Validación de expresiones regulares")
        label.pack(side=TOP)
        self.raiz.iconbitmap("icon.ico")
        self.raiz.config(bg="white")
        self.raiz.config(bg="white", bd=25, relief="groove")


        self.textos = Frame(self.raiz)
        self.textos.pack(side=TOP)
        self.frameDeAbajo = Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)

        self.t1 = Entry(self.textos, width=40)
        self.t1.grid(row=0, column=0, padx=10, pady=10)
        self.t2 = Entry(self.textos, width=40,)
        self.t2.grid(row=1, column=0)
        self.t3 = Entry(self.textos, width=40)
        self.t3.grid(row=2, column=0)
        self.t4 = Entry(self.textos, width=40)
        self.t4.grid(row=3, column=0)
        self.ipv4txt = Entry(self.textos, width=40)
        self.ipv4txt.grid(row=6, column=0, padx=10, pady=10)

        self.b1 = Button(self.textos,text='Validar', command=lambda:self.validar(1))
        self.b1.grid(row=0, column=1,padx=10, pady=10)
        self.b2 = Button(self.textos,text='Validar', command=lambda:self.validar(2))
        self.b2.grid(row=1, column=1, pady=10)
        self.b3 = Button(self.textos,text='Validar', command=lambda:self.validar(3))
        self.b3.grid(row=2, column=1, pady=10)
        self.b4 = Button(self.textos,text='Validar', command=lambda:self.validar(4))
        self.b4.grid(row=3, column=1, pady=10)
        self.b5 = Button(self.textos,text='Generar IPV4', command=lambda:self.ipv4txt.insert(0,self.generar_ipv4()))
        self.b5.grid(row=6, column=1, pady=10)

        self.l1 = Label(self.textos, text="...")
        self.l1.grid(row=0, column=2)
        self.l2 = Label(self.textos, text="...")
        self.l2.grid(row=1, column=2)
        self.l3 = Label(self.textos, text="...")
        self.l3.grid(row=2, column=2)
        self.l4 = Label(self.textos, text="...")
        self.l4.grid(row=3, column=2)


        self.bsalir = Button(self.frameDeAbajo, text="Salir", command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDeAbajo, text="Limpiar", command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        self.raiz.mainloop()

    def limpiar(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.ipv4txt.delete(0, END)
        self.l1.config(fg="black",text="...")
        self.l2.config(fg="black",text="...")
        self.l3.config(fg="black",text="...")
        self.l4.config(fg="black",text="...")
    
    def validar(self, num):
        
        if num == 1:
            txtAvalidar = self.t1.get()
        elif num == 2:
            txtAvalidar = self.t2.get()
        elif num == 3:
            txtAvalidar = self.t3.get()
        elif num == 4:
            txtAvalidar = self.t4.get()

        x = re.search("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",txtAvalidar)
        if x:
            if num == 1:
                self.l1.config(fg="green",text="IPv4 válida")
            elif num == 2:
                self.l2.config(fg="green",text="IPv4 válida")
            elif num == 3:
                self.l3.config(fg="green",text="IPv4 válida")
            elif num == 4:
                self.l4.config(fg="green",text="IPv4 válida")
        else:
            if num == 1:
                self.l1.config(fg="red",text="IPv4 no válida")
            elif num == 2:
                self.l2.config(fg="red",text="IPv4 no válida")
            elif num == 3:
                self.l3.config(fg="red",text="IPv4 no válida")
            elif num == 4:
                self.l4.config(fg="red",text="IPv4 no válida")
    
    def generar_ipv4(self):
        self.ipv4txt.delete(0, END)
        ip = []
        for i in range(4):
            ip.append(str(random.randint(0, 255)))
        return ".".join(ip)
    
        
if __name__ == "__main__":
    app = App()
