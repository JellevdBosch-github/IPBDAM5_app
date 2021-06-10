from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_candlestick
from . import api_candlestick


OHLC = [
	{
		'candlestick_id': '1',
		'timestamp': '1623307985000',
		'open': 123,
		'high': 145,
		'low': 118,
		'close': 140
	},
	{
		'candlestick_id': '2',
		'timestamp': '1623311585000',
		'open': 140,
		'high': 155,
		'low': 138,
		'close': 150
	},
	{
		'candlestick_id': '3',
		'timestamp': '1623315185000',
		'open': 150,
		'high': 152,
		'low': 141,
		'close': 144
	},
]


def abort_not_found(candlestick_id):
	if not any(candlestick['candlestick_id'] == candlestick_id for candlestick in OHLC):
		abort(
			404,
			message={
				'status': 'failed',
				'endpoint': '/api/candlestick/<candlestick_id>',
				'request_method': 'get',
				'error_message': f'No candlestick found matching the given id ({candlestick_id})!'
			}
		)


class Candlestick(Resource):
	"""
	Returns the candlestick with the given id
	"""

	@staticmethod
	def get(candlestick_id):
		abort_not_found(candlestick_id)
		# c = [candle for candle in OHLC if candle['candlestick_id'] == candlestick_id]
		# print(c)
		return jsonify(
			status='success',
			endpoint='/api/candlestick/<candlestick_id>',
			request_method='get',
			candlestick=[candle for candle in OHLC if candle['candlestick_id'] == candlestick_id]
		)


api_candlestick.add_resource(Candlestick, '/<candlestick_id>')


class BrowseCandlesticks(Resource):
	"""
	Returns all candlesticks (optionally up to e certain point in time) as a list of objects
	"""

	@staticmethod
	def get():
		return jsonify(
			status='success',
			endpoint='/api/candlestick/browse',
			request_method='get',
			candlesticks=[candle for candle in OHLC]
		)


api_candlestick.add_resource(BrowseCandlesticks, '/browse')
