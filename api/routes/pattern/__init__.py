from flask import Blueprint
from flask_restful import Api


module_pattern = Blueprint('pattern', __name__, url_prefix='/api/pattern')
api_pattern = Api(module_pattern)


from .controller import *
