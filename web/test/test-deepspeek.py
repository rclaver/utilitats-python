#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, Response
import time

app = Flask(__name__)

def leer_archivo():
    with open('static/arxiu.txt', 'r') as f:
        for linea in f:
            time.sleep(1)
            yield linea

@app.route('/')
def index():
    return render_template('deepspeek.html')

@app.route('/stream')
def stream():
    return Response(leer_archivo(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)