from flask_restful import Resource

class Healthcheck(Resource):
    def get(self):
        return {'message': 'healthcheck ok!'}