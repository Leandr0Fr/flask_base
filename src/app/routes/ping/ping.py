from flask_restx import Resource, Namespace
from flask import make_response, jsonify

ns_ping = Namespace("ping")

@ns_ping.route("")
@ns_ping.doc(responses={200: "API on!"})
class Ping(Resource):
    def get(self):
        return response_generation({"message": "API on!"}, 200)
    
def response_generation(response_data, status):
    response = make_response(jsonify(response_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = status
    return response