from datetime import datetime, timedelta
from flask import request, abort, make_response, jsonify
from shared import jwt_config
from shared import log
import jwt, traceback

class Auth:
    
    def authenticate(self, f):
        def decorator(*args, **kwargs):
            try:
                if not 'Authorization' in request.headers:
                    raise(401)
        
                sensor_id = None
                data = request.headers['Authorization'].encode('ascii','ignore')
                
                token = str.replace(str(data), 'Bearer ','')
            
                
                payload = jwt.decode(token, jwt_config['secret'], algorithms=jwt_config['algo'])
                
                print('data:{}, token:{}, payload:{}'.format(data,token,payload))
                sensor_id = payload['sensor_id']
                
            except Exception as e: #NOTE: can't catch KeyboardInterrupt and SystemExit
                log.error(traceback.format_exc())
                
                return abort(make_response(jsonify(
                    string_code='AUTHENTICATION_FAILED',
                    message='Authentication has failed.',
                    data=None
                ),401))

            return f(sensor_id, *args, **kwargs)     
        return decorator