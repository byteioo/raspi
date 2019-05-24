from flask import Blueprint, jsonify,render_template
from led.pkg import led as L
import time
import datetime


led=Blueprint('led',__name__)

@led.route('/api/<task>/',methods=['GET'])
def dht_api(task):
    if task=="open":
        L.led.open()
    if task=="close":
        L.led.close()

    return jsonify({'error':'false','desc':'完成'})

