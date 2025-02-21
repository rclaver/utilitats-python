#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:32:05 2025
@author: rafael

Las aplicaciones Python con Flask deben ejecutarse desde una terminal.
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

Ejecutar en la nube:
- subir el repositorio a Github
- crear una aplicación en dashboard.render.com
"""
import os, re
from flask import Flask, render_template, request
#from dotenv import load_dotenv

def crear_app():
   app = Flask(__name__) #instancia de Flask
   key_secret = os.getenv("API_KEY")

   @app.route("/index")
   def index():
      return render_template("index.tpl")

   @app.route("/apuntador", methods = ["GET", "POST"])
   def apuntador():
      global escena
      if request.method == "POST":
         escena = request.form.get("seleccio_escenes")
      if escena:
         return render_template("apuntador.tpl", actor=escena)
      else:
         return render_template("index.tpl")

   # -----------------
   # variables globals
   #
   titol = "casats"
   escena = ""
   actor = ""
   sencer = False

   pattern_person = "^(\w*?\s?)(:\s?)(.*$)"
   pattern_narrador = "([^\(]*)(\(.*?\))(.*)"

   dir_dades = "dades"
   base_arxiu_text = titol
   dir_sortida = f"sortides/{titol}/estudi/"
   tmp3 = dir_sortida + "temp.mp3"
   twav = dir_sortida + "temp.wav"

   seq_fragment = 0  #numero sequencial per a la generacio del nom d'arxiu wav de sortida d'una sentencia
   seq_actor = 0     #numero sequencial per a la generacio del nom d'arxiu wav temporal de la veu de l'actor
   pendent_escolta = False  #indica si ha arribat el moment d'escoltar l'actor

   Personatges = {'Joan':   {'speed': 1.18, 'grave': 3.2, 'reduction': 0.6},
                  'Gisela': {'speed': 1.30, 'grave': 0.9, 'reduction': 1.0},
                  'Mar':    {'speed': 1.40, 'grave': 0.7, 'reduction': 1.0},
                  'Emma':   {'speed': 1.40, 'grave': 0.7, 'reduction': 1.0},
                  'Tina':   {'speed': 1.25, 'grave': 1.1, 'reduction': 0.9},
                  'Justa':  {'speed': 1.30, 'grave': 1.2, 'reduction': 0.8},
                  'Pompeu': {'speed': 1.30, 'grave': 2.3, 'reduction': 0.7},
                  'Canut':  {'speed': 1.40, 'grave': 2.1, 'reduction': 0.8}}
   Narrador = {'speed': 1.40, 'grave': 1.8, 'reduction': 1.3}

   """
   Parteix la sentència en fragments que puguin ser processats per gTTs
   @type text: string; text que es tracta
   @type to_veu: list; paràmetres de veu
   @type ends: string; caracter de finalització de la funció print
   """
   def Fragments(text, escena, to_veu, ends):
      global seq_fragment, seq_actor, pendent_escolta
      long_text = len(text)
      ini = 0
      while ini < long_text:
         long_max = 600
         if long_max < long_text:
            long_max = text[ini:].find(" ", long_max)
         if long_max == -1 or long_max > long_text:
            long_max = long_text
         text = text[ini:ini+long_max]

         seq_fragment += 1
         if text == actor:
            pendent_escolta = True
            MostraSentencia(text, ends)
         elif pendent_escolta == True:
            pendent_escolta = False
            seq_actor += 1
            EscoltaActor(text, GeneraNomArxiuWav(escena,True))
            break
         else:
            TextToAudio(text, GeneraNomArxiuWav(escena), to_veu, ends)

         ini += long_max

   '''
   Lectura del text sencer o de l'escena seleccionada de l'obra
   Partició del text en sentències (una sentència correspón a una línia del text)
   Cada sentència pot pertanyer, bé al narrador, bé a un personatge
   '''
   def Proces(escena=""):
      arxiu = f"{dir_dades}/{base_arxiu_text}{escena}.txt"
      escena = f"_{escena}_" if escena else "_"

      with open(arxiu, 'r', encoding="utf-8") as f:
         sentencies = f.read().split('\n')

      for sentencia in sentencies:
         if sentencia:
            # extraure el personatje ma(1) i el text ma(3)
            ma = re.match(pattern_person, sentencia)
            if ma:
               personatje = ma.group(1)
               Fragments(personatje, escena, "narrador", ": ")
               to_veu = Personatges[personatje] if personatje in Personatges else "narrador"
               # extraure, del text ma(3), els comentaris del narrador
               mb = re.match(pattern_narrador, ma.group(3))
               if mb:
                  if mb.group(1) and mb.group(2) and mb.group(3):
                     Fragments(mb.group(1), escena, to_veu, " ")
                     Fragments(mb.group(2), escena, "narrador", " ")
                     Fragments(mb.group(3), escena, to_veu, "\n")
                  elif mb.group(1) and mb.group(2):
                     Fragments(mb.group(1), escena, to_veu, " ")
                     Fragments(mb.group(2), escena, "narrador", "\n")
                  elif mb.group(2) and mb.group(3):
                     Fragments(mb.group(2), escena, "narrador", " ")
                     Fragments(mb.group(3), escena, to_veu, "\n")
               else:
                  Fragments(ma.group(3), escena, to_veu, "\n")
            else:
               Fragments(sentencia, escena, "narrador", "\n")

   @app.route("/play", methods = ["GET", "POST"])
   def play():
      global escena, base_arxiu_text
      if request.method == "POST":
         escena = request.form.get("escena")
      if escena == "sencer":
         Proces("")
      else:
         base_arxiu_text += f"-{actor}-"
         escenes = os.listdir(f"{dir_dades}/{base_arxiu_text}*")
         for escena in escenes:
            Proces(escena)

      return render_template("apuntador.tpl", actor=escena)


   return app

if __name__ == "__main__":
   '''
   Permet la creació de l'aplicació a GitHub
   '''
   app = crear_app()
   '''
   Inicia los servicios flask en la terminal, lo cual, activa el acceso web
   equivale a ejecutar en una terminal el comando: flask run
   así, se activa el reconocimento de las aplicaciones Python en el puerto 5000 de localhost
   '''
   app.run()
