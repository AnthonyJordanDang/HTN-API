from flask_restful import Resource, reqparse

class UserData(Resource):
    def get(self, id):
        return {
            'message' : 'This is working!'
        }

