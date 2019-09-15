from flask_restful import Resource, reqparse

class UserData(Resource):
    def get(self, user_id):
        global uid
        global tdapi
        uid = user_id
        tdapi.
        return {
            'Status' : 'Welcome to the club'
        }

