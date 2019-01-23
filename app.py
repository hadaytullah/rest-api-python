import os
from flask import Flask
import jwt
from api.sensor import Sensor
from api.data import Data
app = Flask(__name__)

#routes        
@app.route('/')
def test():
    return 'API is alive.'

sensor_view_func = Sensor().as_view('sensor')
app.add_url_rule('/sensors/', defaults={'sensor_id':None}, view_func=sensor_view_func, methods=['GET',])
app.add_url_rule('/sensors/', view_func=sensor_view_func, methods=['POST',])
app.add_url_rule('/sensors/<sensor_id>/', view_func=sensor_view_func, methods=['GET', 'PUT', 'DELETE'])
#app.add_url_rule('/sensor/<sensor_id>/data', view_func=data_view_func, methods=['POST',])

data_view_func = Data().as_view('data')
#app.add_url_rule('/data/', defaults={'sensor_id':None}, view_func=data_view_func, methods=['GET',])
app.add_url_rule('/data/', view_func=data_view_func, methods=['POST',])
#app.add_url_rule('/data/<sensor_id>/', view_func=data_view_func, methods=['GET', 'PUT', 'DELETE'])

#start the api server
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))