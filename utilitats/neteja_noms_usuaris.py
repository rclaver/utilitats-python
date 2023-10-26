#!/usr/bin/python3
# -*- coding: UTF8 -*-
# Created on : 26 oct. 2023, 12:14:21
# Author     : rafael
# Script per a la neteja dels noms d'usuari en els arxius de projectes
import os, sys, socket, shutil
import re

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
    RUN_DIR="~/Vídeos"
else:
    RUN_DIR="~/wiki18/data/mdprojects"	# servidor dokuwiki

LOG = RUN_DIR+"/resultat_neteja_noms_usuaris.txt"

# Establecer el directorio RUN_DIR como directorio actual
os.chdir(RUN_DIR)
RUN_DIR = "."

# Recorre recursivamente el directorio RUN_DIR buscando los archivos de proyecto 'meta.mdpr'
# A continuación limpia
def voltarDirectori():

    # Voltar el directori per obtenir tots els seus elements que han de ser tractats
    def voltaLinks(log, dir):
        slist = os.listdir(dir)
        slist.sort()

        for file in slist:
            actual = dir+"/"+file
            if (os.path.isdir(actual)):
                voltaLinks(log, actual)
                log.write("- directori " + actual + "\n")
            elif (file=='meta.mdpr' and os.path.isfile(actual)):
                arxiu = open(actual, "r")
                s = re.search('"(autor|creador|responsable)":(".*?")', arxiu)
                re.sub(r'"(autor|creador|responsable)":(".*?")', '"\1":\2', arxiu)
                log.write("-- hallado en " + actual + ": " + s[0] + "\n")

        return

    listFiles = os.listdir(RUN_DIR)
    listFiles.sort()
    log = open(LOG, "a")

    for d in listFiles:
        print("directori "+CB_GRN+d+C_NONE)
        log.write("directori " + d + "\n")
        voltaLinks(log, d)
        log.close()

    return

# ----
# main
# ----
voltarDirectori()
print("=== FI ===")
