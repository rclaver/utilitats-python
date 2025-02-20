#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Creat: 19-02-2025
@author: rafael claver
@description: Programa interactiu per estudiar i practicar un personatge d'una obra de teatre

pip install -r requirements.txt
pip install gTTS
pip install pydub
pip install soundfile
pip install playsound
pip install pyworld
pip install SpeechRecognition
"""

# -----------------
# variables globals
#
titol = "casats"
escenes = ""
actor = ""
sencer = False

dir_dades = "dades"
base_arxiu_text = titol if sencer else f"{titol}-{actor}-"
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

# --------
# funcions
#

def index(req):
   html = open("/var/www/apuntador/plantilles/index.tpl").read()
   return html
