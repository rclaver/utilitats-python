#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:39:22 2025
@author: rafael
"""
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('openai1.html')

@app.route('/get_line')
def get_line():
    # Aquí podrías abrir el archivo y leer línea por línea
    with open('../dades/casats-joan-01.txt', 'r') as f:
        lines = f.readlines()

    # Simulamos que cada línea se obtiene con un pequeño delay
    for line in lines:
        time.sleep(1)  # Simula un retraso de 1 segundo
        yield f"data: {line}\n\n"

if __name__ == '__main__':
    app.run(debug=True)

