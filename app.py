from flask import Flask, request, jsonify
from flask_restful import Api
from flask import jsonify
from views import views
from resources import resources 
from flask_cors import CORS 
from views import views
import threading
from ingest import TDApi

app = Flask(__name__)
api = Api(app)

tdapi = TDApi()

uid = None
transactions = None

def update_transactions():
    # start this by calling it once we get the UID
    threading.Timer(15, update_transactions).start()
    transactions = tdapi.get_past_transactions(uid)

CORS(app)

#API HOME PAGE

app.register_blueprint(views.default_page)

#User resources
api.add_resource(resources.UserData, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
