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
        print(request.data)
        return jsonify(
                 code='200',
                 message='Sensor registered ' + sensorid + '.',
                 payload=request.data
                )   
    
    #def put(self):
    #def delete(self):
        