from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_candlestick
from . import api_candlestick
from database.services import candlestick as service


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
			candlesticks=[candle for candle in service.browse()]
		)


api_candlestick.add_resource(BrowseCandlesticks, '/browse')


class BrowseCandlesticksEndtime(Resource):
	"""
	Returns all candlesticks (optionally up to e certain point in time) as a list of objects
	"""

	@staticmethod
	def get(timestamp):
		return jsonify(
			status='success',
			endpoint='/api/candlestick/browse/:timestamp',
			request_method='get',
			candlesticks=[candle for candle in service.browse(timestamp)]
		)


api_candlestick.add_resource(BrowseCandlesticksEndtime, '/browse/<timestamp>')


class CountCandlesticks(Resource):
	"""
	Returns the amount of candlesticks as a int
	"""

	@staticmethod
	def get():
		return jsonify(
			status='success',
			endpoint='/api/candlestick/count',
			request_method='get',
			count=service.count()
		)


api_candlestick.add_resource(CountCandlesticks, '/count')
