from flask import Flask
from flask_restful import Api
from flask import jsonify
from views import views
from resources import resources 
from flask_cors import CORS
from views import views

app = Flask(__name__)
api = Api(app)

CORS(app)

#API HOME PAGE
app.register_blueprint(views.default_page)

#User resources
api.add_resource(resources.UserData, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
