from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_trade
from . import api_trade


TRADES = [
	{
		'trade_id': '1A',
		'original': 1,
		'original_id': None,
		'price': 100.00,
		'quantity': 12,
		'eur_value': 100.00,
		'usd_value': 121.85,
		'doge_value': 362.062222,
		'timestamp': '1623323973068',
		'pattern': 'bull1',
		'taker_side': 0,
		'wallet_value': 10000
	},
	{
		'trade_id': '1B',
		'original': 0,
		'original_id': '1A',
		'price': 368.63725344,
		'quantity': 12,
		'eur_value': 102.00,
		'usd_value': 124.29,
		'doge_value': 368.63725344,
		'timestamp': '1623325159000',
		'taker_side': 1,
		'wallet_value': 9998
	},
]


def abort_not_found(trade_id):
	if not any(trade['trade_id'] == trade_id for trade in TRADES):
		abort(
			404,
			message={
				'status': 'failed',
				'endpoint': '/api/trade/<trade_id>',
				'request_method': 'get',
				'error_message': f'No trade found matching the given id ({trade_id})!'
			}
		)


class Trade(Resource):
	"""
	Retrieve a trade by given id
	"""

	@staticmethod
	def get(trade_id):
		abort_not_found(trade_id)
		return jsonify(
			status='success',
			endpoint='api/trade/<trade_id>',
			request_method='get',
			trade=[trade for trade in TRADES if trade['trade_id'] == trade_id]
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
			trades=[trade for trade in TRADES]
		)


api_trade.add_resource(BrowseTrades, '/browse')


class CountTrades(Resource):
	"""
	Retrieve all trades
	"""

	@staticmethod
	def get():
		amount_long = sum(trade['taker_side'] == 1 for trade in TRADES)
		amount_short = sum(trade['taker_side'] == 0 for trade in TRADES)
		return jsonify(
			status='success',
			endpoint='/api/trade/count',
			request_method='get',
			count=len(TRADES),
			amount_long=amount_long,
			amount_short=amount_short
		)


api_trade.add_resource(CountTrades, '/count')

