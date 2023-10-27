#!/usr/bin/python3
# -*- coding: UTF8 -*-
# Created on : 26 oct. 2023, 12:14:21
# Author     : rafael
# Script per a la neteja dels noms d'usuari en els arxius de projectes
import os, sys, socket
import re
import json

C_NONE="\033[0m"
C_CYN="\033[0;36m"  #normal
CB_GRN="\033[1;32m"
CB_CYN="\033[1;36m"

print(sys.version_info)
print("hostname: "+socket.gethostname())
print(CB_CYN+"=====================================================================")
print(CB_CYN+" Script per a la neteja dels noms d'usuari en els arxius de projectes")
print(CB_CYN+"====================================================================="+C_NONE)

# Valors per defecte
if (socket.gethostname() == "LM19"):
    RUN_DIR="/home/rafael/Vídeos"
elif (socket.gethostname() == "anaconda21"):
    RUN_DIR="/home/rafael/Descargas"
else:
    RUN_DIR="/home/dokuwiki/wiki18/data/mdprojects"	# servidor dokuwiki

LOG = RUN_DIR+"/neteja_noms_usuaris.log"
log = open(LOG, "a")

# Establecer el directorio RUN_DIR como directorio actual
os.chdir(RUN_DIR)
RUN_DIR = "."

def remove_whitespace(data, keys, replace=False):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = remove_whitespace(value, keys, key in keys)
    elif replace:
        data = data.replace(' ', '')

    return data

# Recorre recursivamente el directorio RUN_DIR buscando los archivos de proyecto 'meta.mdpr'
# A continuación limpia
def voltaDirectori(dir):

    listFiles = os.listdir(dir)
    listFiles.sort()

    for file in listFiles:
        actual = dir+"/"+file
        print("arxiu "+CB_GRN+actual+C_NONE)
        log.write("arxiu "+actual+"\n")

        if (os.path.isdir(actual)):
            voltaDirectori(actual)
        elif (file=='meta.mdpr' and os.path.isfile(actual)):
            #f = open(actual, "r")
            #data = f.read()
            #pattern = '"(autor|coordinador|creador|responsable|supervisor)":"(?:(\w)?(\s*,?))*"'
            #pattern = '"(AUT|CRE|RES|SUP)":"(\w*)(\s*)(,*)"'
            #s = re.search(pattern, data)
            #re.sub(r pattern, '"\1":\2', data)
            f = open(actual, "r")
            data = f.read()
            keys = ['autor','coordinador','creador','responsable','supervisor']
            result = json.dumps(remove_whitespace(json.loads(data), keys))
            f = open(actual+".result", "w")
            f.write(result)

    return

# ----
# main
# ----
voltaDirectori(RUN_DIR)
log.close()
print("=== FI ===")
