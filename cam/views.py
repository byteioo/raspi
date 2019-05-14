from flask import Blueprint, jsonify
from flask import render_template
from cam.pkg import config
from cam.pkg import sg90

from flask import request

webcam=Blueprint('cam',__name__)
@webcam.route('/',methods=['GET'])
def cam_index():
    params = {
        "WIDTH": config.V_WIDTH,
        "HEIGHT": config.V_HEIGHT,
        "WS_TOKEN": config.WS_TOKEN,
        "WS_URL": config.WS_URL
    }
    return render_template('picamera.html',**params)


@webcam.route('/api/<task>/',methods=['GET'])
def cam_sg90(task):
    commend=["left","right","reset","up","down"]
    if task not in commend:
        return jsonify({
            'error': 'true',
            'desc': {
                '状态': "你干啥呢？"
            }
        })
    if task =="down":
        sg90.vertical_steer.forwardRotation()
    if task =="up":
        sg90.vertical_steer.reverseRotation()
    if task == "left":
        sg90.horizontal_steer.forwardRotation()
    if task == "right":
        sg90.horizontal_steer.reverseRotation()
    if task == "reset":
        sg90.horizontal_steer.reset()
        sg90.vertical_steer.reset()

    return jsonify({
        'error': 'false',
        'desc': {
            '状态': "已旋转,当前角度："+str(sg90.horizontal_steer.position)
        }
    })
