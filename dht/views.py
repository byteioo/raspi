from flask import Blueprint, jsonify,render_template
from dht.pkg import dht11
import time
import datetime


dht=Blueprint('dht',__name__)
instance = dht11.DHT11(pin=18)

@dht.route('/api',methods=['GET'])
def dht_api():
    i=8
    while i > 0:
        result = instance.read()
        if result.is_valid():
            return jsonify({
                'error':'false',
                'desc':{
                    'datetime': str(datetime.datetime.now())[:-7],
                    'temperature':result.temperature,
                    'humidity':result.humidity
                }
            })
        time.sleep(1)
        i=i - 1
    return jsonify({'error':'true','desc':'获取DHT11数据失败'})

@dht.route('/',methods=['GET'])
def dht_index():
    i=8
    params = {
        "datetime": str(datetime.datetime.now())[:-7],
        "status": "fail",
        "temperature": "null",
        "humidity": "null"
    }
    while i > 0:
        result = instance.read()
        if result.is_valid():
            params["datetime"] = str(datetime.datetime.now())[:-7]
            params["status"] = "success"
            params["temperature"] = result.temperature
            params["humidity"] = result.humidity
            break
        time.sleep(1)
        i = i - 1
    return render_template('dht.html', **params)
