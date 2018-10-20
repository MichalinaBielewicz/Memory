from tkinter import *
from time import sleep
import time
import random

master = Tk()
button_switch = True


def close_window(wygrana):
   master.destroy()
   wygrana.destroy()


lista = [0]

def click(b1, b2, b3, b4, b5, b6, b7, b8, txt,lista, id):
   lista.append(id)
   if lista[len(lista)-2] == 1:
       poprzedni=b1
   elif lista[len(lista)-2] == 2:
       poprzedni=b2
   elif lista[len(lista) - 2] == 3:
       poprzedni = b3
   elif lista[len(lista) - 2] == 4:
       poprzedni = b4
   elif lista[len(lista) - 2] == 5:
       poprzedni = b5
   elif lista[len(lista) - 2] == 6:
       poprzedni = b6
   elif lista[len(lista) - 2] == 7:
       poprzedni = b7
   elif lista[len(lista) - 2] == 8:
       poprzedni = b8

   if lista[len(lista)-1]==1:
       aktualny=b1
   elif lista[len(lista)-1]==2:
       aktualny=b2
   elif lista[len(lista)-1] == 3:
       aktualny = b3
   elif lista[len(lista)-1] == 4:
       aktualny = b4
   elif lista[len(lista)-1] == 5:
       aktualny = b5
   elif lista[len(lista)-1] == 6:
       aktualny = b6
   elif lista[len(lista)-1] == 7:
       aktualny = b7
   elif lista[len(lista)-1] == 8:
       aktualny = b8

   aktualny["text"] = txt

   if lista[len(lista)-2] != 0 and poprzedni["text"] != " " and poprzedni["state"] != DISABLED:
       if aktualny["text"] == poprzedni["text"] and aktualny != poprzedni:
           aktualny["state"] = DISABLED
           aktualny["background"] = "lightgray"
           poprzedni["state"] = DISABLED
           poprzedni["background"] = "lightgray"
       elif aktualny["text"] != poprzedni["text"]:
           aktualny["text"] = " "
           poprzedni["text"] = " "

   if b1["state"] == DISABLED and b2["state"] == DISABLED and b3["state"] == DISABLED and b4["state"] == DISABLED and b5["state"] == DISABLED and b6["state"] == DISABLED and b7["state"] == DISABLED and b8["state"] == DISABLED:
       wygrana = Tk()
       button = Button(wygrana, text="BRAWO", background="yellow", command=lambda: close_window(wygrana))
       button.pack()


#losowanie pozycji
pozycja=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3]]
pomocny= [0,1,2,3,4,5,6,7]
pomocny = random.sample(pomocny, k=len(pomocny))

b1 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Goodbye", lista, 1), background="skyblue", width=8, height=5, state=NORMAL)
b1.grid(row=pozycja[pomocny[0]][0], column=pozycja[pomocny[0]][1])
b2 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Goodbye", lista, 2), background="skyblue", width=8, height=5, state=NORMAL)
b2.grid(row=pozycja[pomocny[1]][0], column=pozycja[pomocny[1]][1])
b3 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Hello", lista, 3), background="skyblue", width=8, height=5, state=NORMAL)
b3.grid(row=pozycja[pomocny[2]][0], column=pozycja[pomocny[2]][1])
b4 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Hello", lista, 4), background="skyblue", width=8, height=5, state=NORMAL)
b4.grid(row=pozycja[pomocny[3]][0], column=pozycja[pomocny[3]][1])
b5 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Bye", lista, 5), background="skyblue", width=8, height=5, state=NORMAL)
b5.grid(row=pozycja[pomocny[4]][0], column=pozycja[pomocny[4]][1])
b6 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Bye", lista, 6), background="skyblue", width=8, height=5, state=NORMAL)
b6.grid(row=pozycja[pomocny[5]][0], column=pozycja[pomocny[5]][1])
b7 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Hi", lista, 7), background="skyblue", width=8, height=5, state=NORMAL)
b7.grid(row=pozycja[pomocny[6]][0], column=pozycja[pomocny[6]][1])
b8 = Button(master, text=" ", command=lambda: click(b1, b2, b3, b4, b5, b6, b7, b8, "Hi", lista, 8), background="skyblue", width=8, height=5, state=NORMAL)
b8.grid(row=pozycja[pomocny[7]][0], column=pozycja[pomocny[7]][1])
mainloop()
