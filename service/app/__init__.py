from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


CORS(app, resources={ r'/*': {'origins': "*"}},  methods=["GET", "POST"])


SWAGGER_URL = '/swagger'  
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  #
        'app_name': "My Flask API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


from view.views import *
