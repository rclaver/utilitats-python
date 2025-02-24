#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:09:32 2025
@author: rafael
"""
from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Variables globales para controlar el flujo de lectura
is_paused = False
stop_reading = False

# Función para leer el archivo línea por línea
def read_file():
    global is_paused, stop_reading
    with open('../dades/casats-joan-01.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if stop_reading:
            break  # Detener la lectura si se ha solicitado
        while is_paused:
            time.sleep(0.1)  # Esperar mientras esté en pausa

        socketio.emit('new_line', {'line': line})  # Enviar la línea al cliente
        time.sleep(1)  # Simular un retraso entre líneas

# Ruta para servir el archivo HTML
@app.route('/')
def index():
    return render_template('thread2.html')

# Evento que se dispara cuando un cliente se conecta
@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

# Evento de "iniciar"
@socketio.on('start')
def handle_start():
    global stop_reading
    stop_reading = False  # Reiniciar la bandera de parada
    threading.Thread(target=read_file).start()

# Evento de "pausar"
@socketio.on('pause')
def handle_pause():
    global is_paused
    is_paused = not is_paused  # Alternar entre pausado y reanudado

# Evento de "detener"
@socketio.on('stop')
def handle_stop():
    global stop_reading
    stop_reading = True  # Detener la lectura del archivo

if __name__ == '__main__':
    socketio.run(app, debug=True)
