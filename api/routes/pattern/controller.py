from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_pattern
from . import api_pattern


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
		'wallet_before': 10000
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
		'wallet_after': 9998
	},
]


class CountPattern(Resource):
	"""
	Returns the amount of different patterns recognized
	"""

	@staticmethod
	def get():
		count = 8
		return jsonify(
			status='success',
			endpoint='/api/pattern/count',
			request_method='get',
			count=count
		)


api_pattern.add_resource(CountPattern, '/count')
