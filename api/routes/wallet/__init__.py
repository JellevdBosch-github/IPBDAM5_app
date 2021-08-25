from flask import Blueprint
from flask_restful import Api


module_wallet = Blueprint('wallet', __name__, url_prefix='/api/wallet')
api_wallet = Api(module_wallet)


from .controller import *
