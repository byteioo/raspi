from flask import Blueprint, jsonify
from flask import render_template
from cam.pkg import config
main=Blueprint('main',__name__)

@main.route("/")
def app_index():  # 主页
  return render_template('index.html')

@main.route("/test")
def app_test():
  params = {
    "WIDTH": config.V_WIDTH,
    "HEIGHT": config.V_HEIGHT,
    "WS_TOKEN": config.WS_TOKEN
  }
  return render_template('picamera.html',**params)
