from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_trade
from . import api_trade
from database.services import trade as service


class Trade(Resource):
	"""
	Retrieve a trade by given id
	"""

	@staticmethod
	def get(trade_id):
		return jsonify(
			status='success',
			endpoint='api/trade/<trade_id>',
			request_method='get',
			trade=[trade for trade in service.get(trade_id)]
		)


api_trade.add_resource(Trade, '/<trade_id>')


class BrowseTrades(Resource):
	"""
	Retrieve all trades
	"""

	@staticmethod
	def get():
		return jsonify(
			status='success',
			endpoint='/api/trade/browse',
			request_method='get',
			trades=[trade for trade in service.browse()]
		)


api_trade.add_resource(BrowseTrades, '/browse')


class CountTrades(Resource):
	"""
	Retrieve all trades
	"""

	@staticmethod
	def get():
		# amount_long = sum(trade['taker_side'] == 1 for trade in TRADES)
		# amount_short = sum(trade['taker_side'] == 0 for trade in TRADES)
		return jsonify(
			status='success',
			endpoint='/api/trade/count',
			request_method='get',
			count=service.count(),
			# amount_long=amount_long,
			# amount_short=amount_short
		)


api_trade.add_resource(CountTrades, '/count')

