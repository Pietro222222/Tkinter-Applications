from tkinter import *
import random
root = Tk()
root.geometry("500x350")
root.minsize(width=500, height=350)
root.maxsize(width=500, height=350)
i = ['⬆️', '⬇️']
isNumber = IntVar()
isLetra = IntVar()
isCaractere = IntVar()
Numeros = Checkbutton(root, text="Numeros", padx=15, pady=15, variable=isNumber)
Letras = Checkbutton(root, text="Letras", padx=15, pady=15, variable=isLetra)
Caracteres = Checkbutton(root, text="Caracteres como #", padx=15, pady=15, variable=isCaractere)
CurrentlySize = 0
LabalSize = Label(root, text=str(CurrentlySize), padx=70, font=('Courier', 44))
def Aumentar():
    global CurrentlySize
    CurrentlySize += 1
    LabalSize = Label(root, text=str(CurrentlySize), padx=70, font=('Courier', 44))
    LabalSize.grid(row=0, column=0, columnspan=5)
def Diminuir():
    global CurrentlySize
    CurrentlySize -= 1
    if(CurrentlySize < 0):
        CurrentlySize = 0
    LabalSize = Label(root, text=str(CurrentlySize), padx=70, font=('Courier', 44))
    LabalSize.grid(row=0, column=0, columnspan=5)
senha = Entry(root, state=DISABLED)
size = Button(root, text=i[0], width=27, command=Aumentar)
size2 = Button(root, text=i[1], width=30, command=Diminuir)
def GenPass():
    generatedPassword = ""
    global CurrentlySize
    c = 0
    chrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    caracs = ['!', '@', '#', '$', '%', '&']
    Chars = []
    
    if(isNumber.get() == 0 and isLetra.get() == 0 and isCaractere.get() == 0):
        return
    if(isLetra.get() == 1):
        for i in range(52):
            Chars.insert(len(Chars), chrs[i])
    if(isNumber.get() == 1):
        for i in range(9):
            Chars.insert(len(Chars), str(i))
    if(isCaractere.get() == 1):
        for i in range(6):
            Chars.insert(len(Chars), caracs[i])
    while(c < CurrentlySize):
        c += 1
        generatedPassword += random.choice(Chars)
    senha = Entry(root, text=generatedPassword, width=25, font=('Courier', 20))
    senha.grid(row=0, column=0, columnspan=5)
    senha.insert(0, str(generatedPassword))
    size.grid_forget()
    size2.grid_forget()
    Letras.grid_forget()
    Numeros.grid_forget()
    Caracteres.grid_forget()
    LabalSize = Label(root, text="")
Gen = Button(root, text="Gerar Senha", command=GenPass, padx=40)
def pack():
    Letras.grid_forget()
    size.grid_forget()
    size2.grid_forget()
    Numeros.grid_forget()
    Caracteres.grid_forget()

    LabalSize.grid(row=0, column=0, columnspan=5)
    size.grid(row=1, column=0)
    size2.grid(row=1, column=1)
    Letras.grid(row=2, column=0)
    Numeros.grid(row=2, column=1)
    Caracteres.grid(row=3, column=0, columnspan=50)
    Gen.grid(row=2, column=0, columnspan=5)
pack()

root.mainloop()