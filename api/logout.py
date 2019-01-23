#author: hadaytullah kundi, hadaytullah@gmail.com
import traceback, json
from flask.views import MethodView
from flask import jsonify
from flask import request
from flask import abort, make_response
from bson.objectid import ObjectId
from shared import db, log

class Logout(MethodView):
    """
        Logout api entry points handler, GET,POST,PUT,DELETE
    """

    def post(self):
        return abort(make_response(jsonify(
            string_code='NOT_IMPLEMENTED',
            message='This api endpoint has not been implemented.',
            data=None
        ),501))
    
    def post_(self):
        try:
            # encode/decode
            print(request.data.decode('utf-8'))
            data_dict = json.loads(request.data.decode('utf-8'))
            # Store data
            document = db.data.insert_one({
                'sensor_id':data_dict['sensor_id'],
                'speed':data_dict['speed'],
                'speed_unit': data_dict['speed_unit'],
                'location':data_dict['location'],
                'location_accuracy':data_dict['location_accuracy'],
            })
            print(document.inserted_id)
            if document.inserted_id: #if inserted successfully
                return jsonify(
                    string_code='DATA_INSERTED',
                    message='Sensor data stored in the database.',
                    data= {
                        'id':document.inserted_id.__str__()
                    }
                )
            else:
                # do not expose what went wrong to the callee, use a logger to log it for internal use
                log.info('Unable to insert data into db')
                log.info(request.data)
                
                return abort(make_response(jsonify(
                    string_code='SERVER_ERROR',
                    message='Something went wrong.',
                    data=None
                ),500))
            
        except Exception as e: #NOTE: can't catch KeyboardInterrupt and SystemExit
            # do not expose what went wrong to the callee, use a logger to log it for internal use
            log.error(traceback.format_exc())
            
            return abort(make_response(jsonify(
                string_code='SERVER_ERROR',
                message='Something went wrong.',
                data=None
            ),500))
            
  