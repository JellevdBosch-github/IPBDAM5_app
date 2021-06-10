from flask import Blueprint
from flask_restful import Api


module_trade = Blueprint('trade', __name__, url_prefix='/api/trade')
api_trade = Api(module_trade)


from .controller import *
