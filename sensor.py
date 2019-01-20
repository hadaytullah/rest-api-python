#author: hadaytullah kundi, hadaytullah@gmail.com
from flask.views import MethodView


class Sensor(MethodView):
    """
        Sensor api entry points handler, GET,POST,PUT,DELETE
    """
    def get(self, sensorid):
        return 'You are sensor ' + sensorid + '.'

    #def post(self):
    #def put(self):
    #def delete(self):
        