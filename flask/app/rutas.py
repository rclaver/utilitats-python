# -*- coding: UTF8 -*-
'''
@created: Thu Nov 24 11:48:17 2022
@author: rafael
@description:
'''

from app import app
@app.route('/')
@app.route('/index')
def index():
   html = "<p><b>Bon dia a tothom</b></p>"
   html += "<p>Se ejecuta desde la linea de comandos:</p>"
   html += "<p>(base) ~/$ cd ~/projectes/Python/flask/</p>"
   html += "<p>(base) ~/projectes/Python/flask/$ flask run</p>"
   html += "<p><br>En la URL del navegador:</p>"
   html += "<p>http://localhost:5000/</p>"
   return html
