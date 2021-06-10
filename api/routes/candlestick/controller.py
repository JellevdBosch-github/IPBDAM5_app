from flask import Blueprint, request
from flask_restful import Resource, Api, request
from utils import datetime
from . import module_candlestick
from . import api_candlestick


class CandlestickController(Resource):

	@staticmethod
	def get(candlestick_id):
		return {
			'status': 'success',
			'endpoint': '/api/candlestick',
			'request_method': 'get',
			'candlestick': {
				'candlestick_id': candlestick_id,
				'open': 123,
				'high': 145,
				'low': 118,
				'close': 140
			}
		}


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
