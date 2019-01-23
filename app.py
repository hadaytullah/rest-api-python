import os
from flask import Flask
import jwt
from api.sensor import Sensor

app = Flask(__name__)

#routes        
@app.route('/')
def test():
    return 'API is alive.'

sensor_view_func = Sensor().as_view('sensor')
app.add_url_rule('/sensor', view_func=sensor_view_func)
app.add_url_rule('/sensor/<sensor_id>', view_func=sensor_view_func)

#start the api server
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))