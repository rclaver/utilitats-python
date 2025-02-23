#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:09:32 2025
@author: rafael
"""

from flask import Flask, render_template
import threading
import time

app = Flask(__name__)

data = ""
C_NONE="\033[0m"
CB_YLW="\033[1;33m"
CB_BLU="\033[1;34m"

@app.route('/sensor')
def index():
    global data
    print(f"{CB_BLU}{data}{C_NONE}")
    return render_template('thread.html', data=data)


def update_data(d):
    global data
    with open('../dades/casats-joan-01.txt', 'r', encoding="utf-8") as f:
       sentencies = f.read().split('\n')

    for sentencia in sentencies:
        data = sentencia
        print(f"{CB_YLW}{data}{C_NONE}")
        time.sleep(1)


if __name__ == '__main__':
    # start updating data
    update_data_thread = threading.Thread(target=update_data, args=(data,))
    update_data_thread.start()
    # start the Flask server
    app.run(host='localhost', port=5000, debug=True)
