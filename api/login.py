#author: hadaytullah kundi, hadaytullah@gmail.com
import traceback, json
from flask.views import MethodView
from flask import jsonify
from flask import request
from flask import abort, make_response
from bson.objectid import ObjectId
from shared import db, log
from datetime import datetime, timedelta
import jwt

#TODO: Store the key as an env variable on production machine
JWT_SECRET = 'Ki39krMoE534' 

JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

class Login(MethodView):
    """
        Login api entry points handler, GET,POST
    """
   
    
    def post(self):
        """
            Handles the login
        """
        try:
            # encode/decode
            data_dict = json.loads(request.data.decode('utf-8'))
            print(data_dict)
    
            user = data_dict['user']
            pwd = data_dict['pwd']
        
            user_data = self.authenticate(user, pwd)
            print(user_data)
            if user_data:
                # valid credentials
                
                # TODO: the transition from user to sensor is a bit confusing, improve please
                payload = {
                    'sensor_id': user_data['sensor_id'],
                    'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
                }
                
                jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
                return jsonify(
                    token = jwt_token.decode('utf-8')
                )
            else:
                # invalid credential
                return abort(make_response(jsonify(
                    string_code = 'AUTHENTICATION_FAILED',
                    message = 'Authentication has failed.',
                    data = None
                ),500))

        except Exception as e: #NOTE: can't catch KeyboardInterrupt and SystemExit
            # do not expose what went wrong to the callee, use a logger to log it for internal use
            log.error(traceback.format_exc())
            
            return abort(make_response(jsonify(
                string_code='SERVER_ERROR',
                message='Something went wrong.',
                data=None
            ),500))
    
    def authenticate(self, user, pwd):
        """
            NOTE!!!
            for testing purpose only, to be removed and replaced with DB calls
            pwd to to be encrypted, use BCRYPT on client and server side
        """
        if user=='sensor' and pwd=='sensor':
            return {
                'sensor_id':'5c48971d9637843ebad8dc13'
            }
        else:
            return None 