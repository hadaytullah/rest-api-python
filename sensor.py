#author: hadaytullah kundi, hadaytullah@gmail.com
from flask.views import MethodView
from flask import jsonify
from flask import request

class Sensor(MethodView):
    """
        Sensor api entry points handler, GET,POST,PUT,DELETE
    """
    def get(self, sensorid):
        return jsonify(
                 code='200',
                 message='Sensor data ' + sensorid + ' returned.'
                )

    def post(self):
        sensorid='002'
        return jsonify(
                 code='200',
                 message='Sensor registered ' + sensorid + '.',
                 data=request.data
                )   
    
    def put(self,sensorid):
        return jsonify(
                 code='200',
                 message='Sensor ' + sensorid + ' info updated.',
                 data=request.data
                )   
    
    def delete(self, sensorid):
        return jsonify(
                 code='200',
                 message='Sensor ' + sensorid + ' removed.',
                )   