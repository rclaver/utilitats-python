#!/usr/bin/python3
# -*- coding: UTF8 -*-
'''
@created: Thu Nov 24 09:41:08 2022
@author: rafael
@description:
'''
from flask import Flask, request
app = Flask(__name__)

ini_div = "<div style='margin:auto; font-family:Arial; border:1px solid gray; width:400px; padding:10px;'"
fin_div = "</div>"

@app.route('/flask_hello')
def benvinguda():
	html = ini_div+"<p style='font:bold 11pt Arial;'>Bon dia a tothom</p>" \
			 "<p style='font:10pt Arial;'>Pàgina d'exemple.<br>" \
			 "Veure la <a href='/flask_desc'>descripció</a><br>" \
			 "Veure els <a href='/flask_method'>métodes</a></p>"+fin_div
	return html

@app.route('/flask_desc')
def descripcio():
	html = ini_div+"<p style='font:bold 11pt Arial;'>Descipción</p>" \
			 "<p style='font:10pt Arial;'>Usando Flask, las modificaciones del fichero fuente no necesitan<br>" \
			 "parar el servidor para que sean trasladadas al clente.<br>" \
			 "Si el parámetro 'debug' tiene el valor 'True', los cambios en el fichero fuente son detectados<br>" \
			 "en el servidor y Flask se encarga de ejecutar un reload con el comando 'stat'.</p>"+fin_div
	return html

@app.route('/flask_method', methods=['GET', 'POST'])
def metodes():
	if request.method == 'POST':
		html = 'Hemos accedido con POST'
	else:
		html = 'Hemos accedido con GET'

	html = ini_div+"<p style='font:bold 11pt Arial;'>Métodes d'accés</p>" \
			 "<p style='font:10pt Arial;'>" + html + "</p>" + fin_div
	return html

if (__name__ == "__main__"):
   app.run(host='0.0.0.0', debug=True, port=8080)
