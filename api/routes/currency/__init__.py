from flask import Blueprint
from flask_restful import Api


module_currency = Blueprint('currency', __name__, url_prefix='/api/currency')
api_currency = Api(module_currency)


from .controller import *
