from flask import jsonify
from flask_restful import Resource, abort
from utils.datetime import get_current_epoch_ms
from . import api_trade


TRADES = [
	{
		'trade_id': '1',
		'original': 1,
		'original_id': None,
		'price': 100.00,
		'quantity': 12,
		'eur_value': 100.00,
		'usd_value': 121.85,
		'doge_value': 362.062222,
		'timestamp': '1623323973068',
		'taker_side': 0
	},
	{
		'trade_id': '2',
		'original': 0,
		'original_id': 1,
		'price': 362.062222,
		'quantity': 12,
		'eur_value': 102.00,
		'usd_value': 124.29,
		'doge_value': 362.062222,
		'timestamp': '1623325159000',
		'taker_side': 1
	},
]


def abort_not_found(trade_id):
	if not any(trade['trade_id'] == trade_id for trade in TRADES):
		abort(
			404,
			message=jsonify(
				status='failed',
				endpoint='/api/trade/<trade_id>',
				request_method='get',
				error_message=f'No trade found matching the given id ({trade_id})!'
			)
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


