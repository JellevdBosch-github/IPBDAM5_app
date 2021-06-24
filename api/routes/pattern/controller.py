from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_pattern
from . import api_pattern


PATTERNS = [
	{
		'pattern': 'bull1',
		'occurences': 3,
		'profit': 5.03
	},
	{
		'pattern': 'bull2',
		'occurences': 13,
		'profit': 3.43
	},
	{
		'pattern': 'bull3',
		'occurences': 41,
		'profit': -2.07
	},
	{
		'pattern': 'bear1',
		'occurences': 70,
		'profit': -5.67
	},
	{
		'pattern': 'bear2',
		'occurences': 3,
		'profit': 10.03
	},
	{
		'pattern': 'bear3',
		'occurences': 11,
		'profit': 4.03
	},
]


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


class BrowsePattern(Resource):
	"""
	Returns the amount of profit per pattern
	"""

	@staticmethod
	def get():
		return jsonify(
			status='success',
			endpoint='/api/pattern/browse',
			request_method='get',
			patterns=[pattern for pattern in PATTERNS]
		)


api_pattern.add_resource(BrowsePattern, '/browse')


class CountPattern(Resource):
	"""
	Returns the amount of different patterns recognized
	"""

	@staticmethod
	def get():
		return jsonify(
			status='success',
			endpoint='/api/pattern/count',
			request_method='get',
			count=len(PATTERNS)
		)


api_pattern.add_resource(CountPattern, '/count')
