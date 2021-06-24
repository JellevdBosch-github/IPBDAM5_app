from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_candlestick
from . import api_candlestick


OHLC = [
	{
		'candlestick_id': '7',
		'timestamp': '1624539599999',
		'open': 0.20326000,
		'high': 0.20539000,
		'low': 0.19966000,
		'close': 0.20281000
	},
	{
		'candlestick_id': '8',
		'timestamp': '1624535999999',
		'open': 0.19586000,
		'high': 0.20363000,
		'low': 0.19586000,
		'close': 0.20318000
	},
	{
		'candlestick_id': '9',
		'timestamp': '1624532399999',
		'open': 0.19941000,
		'high': 0.20000000,
		'low': 0.19561000,
		'close': 0.19593000
	},
	{
		'candlestick_id': '10',
		'timestamp': '1624528799999',
		'open': 0.20027000,
		'high': 0.20125000,
		'low': 0.19755000,
		'close': 0.19897000
	},
	{
		'candlestick_id': '11',
		'timestamp': '1624525199999',
		'open': 0.19520000,
		'high': 0.19520000,
		'low': 0.19520000,
		'close': 0.19983000
	},
	{
		'candlestick_id': '12',
		'timestamp': '1624521599999',
		'open': 0.19629000,
		'high': 0.19995000,
		'low': 0.19455000,
		'close': 0.19492000
	},
	{
		'candlestick_id': '1',
		'timestamp': '1624543199999',
		'open': 0.20270000,
		'high': 0.20300000,
		'low': 0.19791000,
		'close': 0.20054000
	},
	{
		'candlestick_id': '2',
		'timestamp': '1624546799999',
		'open': 0.20065000,
		'high': 0.20133000,
		'low': 0.19800000,
		'close': 0.20123000
	},
	{
		'candlestick_id': '3',
		'timestamp': '1624550399999',
		'open': 0.20130000,
		'high': 0.20635000,
		'low': 0.19980000,
		'close': 0.20096000
	},
	{
		'candlestick_id': '4',
		'timestamp': '1624553999999',
		'open': 0.20071000,
		'high': 0.20487000,
		'low': 0.19881000,
		'close': 0.20483000
	},
	{
		'candlestick_id': '5',
		'timestamp': '1624557599999',
		'open': 0.20484000,
		'high': 0.20749000,
		'low': 0.20315000,
		'close': 0.20588000
	},
	{
		'candlestick_id': '6',
		'timestamp': '1624561199999',
		'open': 0.20610000,
		'high': 0.20968000,
		'low': 0.20490000,
		'close': 0.20914000
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


class BrowseCandlesticksEndtime(Resource):
	"""
	Returns all candlesticks (optionally up to e certain point in time) as a list of objects
	"""

	@staticmethod
	def get(timestamp):
		candles = []
		for candle in OHLC:
			if int(candle['timestamp']) < int(timestamp):
				candles.append(candle)
		return jsonify(
			status='success',
			endpoint='/api/candlestick/browse/:timestamp',
			request_method='get',
			candlesticks=candles
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
			count=len(OHLC)
		)


api_candlestick.add_resource(CountCandlesticks, '/count')
