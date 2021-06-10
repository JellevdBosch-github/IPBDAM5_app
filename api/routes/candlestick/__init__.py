from flask import Blueprint
from flask_restful import Api


module_candlestick = Blueprint('candlestick', __name__, url_prefix='/api/candlestick')
api_candlestick = Api(module_candlestick)


from .controller import *
