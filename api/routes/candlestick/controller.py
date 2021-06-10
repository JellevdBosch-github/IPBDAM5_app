from flask import Blueprint, request
from utils import datetime


module_candlestick = Blueprint('candlestick', __name__, url_prefix='/api/candlestick')


@module_candlestick.route('/browse', methods=['GET'])
def browse_candlesticks():
	pass
	# response_object = {
	# 	'status': 'Failed',
	# 	'error': 'Invalid request header',
	# 	'description': 'This endpoint requires a GET request'
	# }


@module_candlestick.route('/browse/<int:timestamp>', methods=['POST'])
def browse_candlesticks(timestamp):
	pass


@module_candlestick.route('/read/', defaults={'candlestick_id': datetime.get_current_epoch_ms()})
@module_candlestick.route('/read/<candlestick_id>', methods=['POST'])
def read_candlestick(candlestick_id):
	pass
