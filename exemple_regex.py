#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 15:13:12 2026
@author: rafael

neteja de text: troba el text entre parèntesi i tracta separadament les parts entre parèntesi i les de fora
"""

import re

text = "Pruden (Tremolant, seriosa.) No sé... jo sempre (pausa) vull fer-ho amb les llums apagades."

def model_1():
   print("MODEL 1")
   patro = re.compile(r'([^(]*)(?:\((.*?)\))?')
   resultats = []
   for match in patro.finditer(text):
       if match.group(1):  # Texto fuera de paréntesis
           resultats.append(match.group(1).strip())
           print(f"text: {match.group(1).strip()}")
       if match.group(2):  # Texto dentro de paréntesis
           resultats.append(f"({match.group(2)})")
           print(f"parentesis:{match.group(2)}")

   # Filtra elements buits
   print("Filtra elements buits")
   resultats = [r for r in resultats if r and r != '']
   print(resultats)

def model_2():
   print("MODEL 2")
   parts = re.split(r'(\(.*?\))', text)
   parts = [p for p in parts if p]
   print(parts)
   for p in parts:
      if p[:1] == "(":
         print(f'parèntesi: {p}')
      else:
         print(f'text: {p}')

model_2()
