#  coding: UTF-8
from flask import Flask
from cam.views import *
from views import *
from dht.views import *
from syst.views import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #返回的json中允许中文
app.register_blueprint(main,url_prefix='/')
app.register_blueprint(webcam,url_prefix='/cam')
app.register_blueprint(dht,url_prefix='/dht')
app.register_blueprint(sys,url_prefix='/sys')


if __name__=='__main__':
  app.run(port=9082)