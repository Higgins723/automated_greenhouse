import flask
import json
from flask import request, jsonify
from pump import pumpControl
from light import lightControl
from fan import fanControl
from moisture import getData

# GPIO | Relay
#--------------
# 16     01    light
# 20     02    pump
# 21     03    fan

app = flask.Flask(__name__)

@app.route('/api/v1/getData', methods=['GET'])
def moisture():
    return jsonify(getData())

@app.route('/api/v1/pump', methods=['POST'])
def pump():
    value = json.loads(request.data.decode('utf-8'))
    return jsonify(pumpControl(value['value']))

@app.route('/api/v1/light', methods=['POST'])
def light():
    value = json.loads(request.data.decode('utf-8'))
    return jsonify(lightControl(value['value']))

@app.route('/api/v1/fan', methods=['POST'])
def fan():
    value = json.loads(request.data.decode('utf-8'))
    return jsonify(fanControl(value['value']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')