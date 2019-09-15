from flask import Flask, request, jsonify
from flask_restful import Api
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_cors import CORS 
import threading
from ingest import TDApi
import json
from flask import Blueprint
from flask import jsonify

app = Flask(__name__)
api = Api(app)

tdapi = TDApi()

uid = None
budget = 0.0
alerts = {}

default_page = Blueprint('default_page', __name__)

@default_page.route('/')
def index():
    return jsonify({'Status':'This site is working'})


class UserData(Resource):
    def get(self, user_id, user_budget):
        uid = user_id
        budget = user_budget
        return {
            'Status' : 'Welcome to the club'
        }


class AlertSystem(Resource):
    def get(self):
        global alerts
        return json.dumps(alerts)


def update():
    # start this by calling it once we get the UID
    threading.Timer(15, update).start()
    transactions = tdapi.split_monthy(tdapi.get_past_transactions(uid))
    current_spent = tdapi.total_monthly_spending(transactions['09'])
    predicted_spent = tdapi.predicted_monthly_spending(transactions['09'])
    if current_spent > budget:
        alerts['OverBudget'] = {'Amount': current_spent - budget}

    elif predicted_spent > budget:
        alerts['PredictedOverBudget'] = {'Amount': predicted_spent - budget}


CORS(app)

#API HOME PAGE

app.register_blueprint(default_page)

#User resources
api.add_resource(UserData, '/user/<int:user_id>')
api.add_resource(AlertSystem, '/alerts/')

if __name__ == '__main__':
    app.run(debug=True)
