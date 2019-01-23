#author: hadaytullah kundi, hadaytullah@gmail.com
import traceback, json
from flask.views import MethodView
from flask import jsonify
from flask import request
from flask import abort, make_response
from bson.objectid import ObjectId
from shared import db, log

class Sensor(MethodView):
    """
        Sensor api entry points handler, GET,POST,PUT,DELETE
    """
    
    def get(self, sensor_id):
        try:
            document = db.sensors.find_one({'_id':ObjectId(sensor_id)})
            if document:
                return jsonify(
                    string_code='FOUND',
                    message='Sensor data ' + sensor_id + ' returned.',
                    data= {
                        'owner': document['owner'],
                        'vehicle': document['vehicle']
                    }
                )
            else:
                log.info('Sensor not found in the database. {}'.format(sensor_id))
                
                return abort(make_response(jsonify(
                    string_code='NOT_FOUND',
                    message='Sensor does not exist.'
                ),404))
        except Exception as e: #NOTE: can't catch KeyboardInterrupt and SystemExit
            
            log.error(traceback.format_exc())
            
            # do not expose what went wrong to the callee
            return abort(make_response(jsonify(
                string_code='SERVER_ERROR',
                message='Something went wrong.',
                data=None
            ),500))
    
    def post(self):
        try:
            # encode/decode
            print(request.data.decode('utf-8'))
            data_dict = json.loads(request.data.decode('utf-8'))
            # Make a new sensor
            document = db.sensors.insert_one({
                'owner':data_dict['owner'],
                'vehicle':data_dict['vehicle']
            })
            print(document.inserted_id)
            if document.inserted_id: #if inserted successfully
                return jsonify(
                    string_code='DATA_INSERTED',
                    message='Sensor stored in the database.',
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
            
        
    def put(self, sensor_id):
        return abort(make_response(jsonify(
            string_code='NOT_IMPLEMENTED',
            message='This api endpoint has not been implemented.',
            data=None
        ),501))
    
    def delete(self, sensor_id):
        return abort(make_response(jsonify(
            string_code='NOT_IMPLEMENTED',
            message='This api endpoint has not been implemented.',
            data=None
        ),501))