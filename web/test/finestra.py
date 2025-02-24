#!/usr/bin/python3
# -*- coding: UTF8 -*-
'''
@created: 11-02-2025 09:51:55
@author: rafael
@description: finestra d'emulació d'una pantalla de mòbil

requisits:
   sudo apt-get install python3-tk
'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# -----------------
# variables globals
#
ample = 324
alt = 576

escenes = []

root = tk.Tk()
root.geometry("324x576")
root.resizable(False, False)
root.title = "L'Apuntador"

seq_num = 1

def setup():
   global seq_text, img_play,img_pausa, img_rec, img_stop, img_anterior, img_seguent
   espai()
   seq_text = tk.Label(root, text=frmt(seq_num))
   seq_text.config(font=("Ubuntu Mono",40), justify="center", fg='white', bg='blue')
   seq_text.pack()
   espai()

   img_anterior = tk.PhotoImage(file="static/img/anterior.png")
   img_play = tk.PhotoImage(file="static/img/play.png")
   img_pausa = tk.PhotoImage(file="static/img/pausa.png")
   img_rec = tk.PhotoImage(file="static/img/rec.png")
   img_stop = tk.PhotoImage(file="static/img/stop.png")
   img_seguent = tk.PhotoImage(file="static/img/seguent.png")

   btn_anterior = ttk.Button(root, image=img_anterior, command=anterior)
   btn_inici   = ttk.Button(root, image=img_play, command=inici)
   btn_pausa = ttk.Button(root, image=img_pausa, command=pausa)
   btn_rec = ttk.Button(root, image=img_rec, command=gravacio)
   btn_stop = ttk.Button(root, image=img_stop, command=stop)
   btn_seguent = ttk.Button(root, image=img_seguent, command=seguent)

   btn_anterior.pack(side=tk.LEFT); btn_anterior.place(x=ample/2-40, y=alt-100)
   btn_inici.pack(side=tk.LEFT); btn_inici.place(x=ample/2, y=alt-100)
   # btn_pausa.pack(side=tk.LEFT); btn_pausa.place(x=ample/2, y=alt-100)
   # btn_rec.pack(side=tk.LEFT); btn_rec.place(x=ample/2, y=alt-100)
   # btn_stop.pack(side=tk.LEFT); btn_stop.place(x=ample/2, y=alt-100)
   btn_seguent.pack(side=tk.RIGHT); btn_seguent.place(x=ample/2+40, y=alt-100)

def inici():
   global seq_num
   seq_num = seq_num + 1
   if seq_num % 5 == 0:
      seq_text.config(fg='white', bg='orange')
      seq_text.config(text=frmt(seq_num))
   else:
      seq_text.config(fg='white', bg='blue')
      seq_text.config(text=frmt(seq_num))

def pausa():
    seq_text.config(text="pausa")

def gravacio():
    seq_text.config(text="gravacio")

def stop():
    seq_text.config(text="stop")

def anterior():
    seq_text.config(text="anterior")

def seguent():
    seq_text.config(text=ample/2)


def missatge(missatge):
   showinfo(message=missatge)

'''
Selecció de les escenes que es vol practicar
'''
def seleccio_escenes():
   escenes = input("Indica les escenes que vols processar: ").lower().split()
   if escenes:
      if escenes == "sencer":
         escenes = []
      elif escenes == "joan":
         escenes = ["102","104","202","204","205","207"]
         print(f"\nEs convertiran les escenes de'n Joan: {escenes}", end='\n\n')
      else:
         escenes = escenes.split()
         print(f"\nEs convertiran les escenes indicades: {escenes}", end='\n\n')
   else:
      escenes = ["101","102","103","104","105","106","201","202","203","204","205","206","207"]
      print(f"\nEs convertiran (per defecte) les escenes: {escenes}", end='\n\n')

   sencer = not (escenes)
   if sencer:
      print("\nEs convertirà l'arxiu sencer", end='\n\n')


def espai():
   espai = tk.Label(root, text="\n")
   espai.config(font=("Sans",20),justify="center")
   espai.pack()

def frmt(n):
   return " "+str(n)+" "

# ---------
# principal
# ---------
if __name__ == "__main__":
   setup()
   root.mainloop()
