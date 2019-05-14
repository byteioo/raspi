from flask import Blueprint, jsonify,render_template
from syst.pkg import sys_util


sys=Blueprint('sys',__name__)

@sys.route('/api',methods=['GET'])
def sys_api():
    return jsonify(sys_util.sysInfo())

@sys.route('/',methods=['GET'])
def sys_index():
    params = sys_util.sysInfo()
    return render_template('syst.html', **params)
