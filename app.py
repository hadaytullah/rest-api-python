import os
from flask import Flask
import jwt
from sensor import Sensor

secret_key = 'Ki39krMoE534'
app = Flask(__name__)

@app.route('/')
def test():
    return 'API is alive.'

#@app.route('/sensor/<string:sensorid>',methods = ['GET'])
#def get_sensor(sensorid):
#    return 'You are sensor ' + sensorid + '.'

app.add_url_rule('/sensor/<string:sensorid>', view_func=Sensor.as_view('sensor'))

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))