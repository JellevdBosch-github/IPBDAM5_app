from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, abort
from utils import datetime
from . import module_currency
from . import api_currency


CURRENCY = [
	{
		"symbol": "DOGE",
		"priceChange": "-94.99999800",
		"priceChangePercent": "-95.960",
		"weightedAvgPrice": "0.29628482",
		"prevClosePrice": "0.10002000",
		"lastPrice": "4.00000200",
		"lastQty": "200.00000000",
		"bidPrice": "4.00000000",
		"askPrice": "4.00000200",
		"openPrice": "99.00000000",
		"highPrice": "100.00000000",
		"lowPrice": "0.10000000",
		"volume": "8913.30000000",
		"quoteVolume": "15.30000000",
		"openTime": 1499783499040,
		"closeTime": 1499869899040
	}
]


def abort_not_found(currency_symbol):
	if not any(currency['symbol'] == currency_symbol for currency in CURRENCY):
		abort(
			404,
			message={
				'status': 'failed',
				'endpoint': '/api/currency/<wallet_id>',
				'request_method': 'get',
				'error_message': f'No currency found matching the given symbol ({currency_symbol})!'
			}
		)


class Currency(Resource):
	"""
	Returns the candlestick with the given id
	"""

	@staticmethod
	def get(currency_symbol):
		abort_not_found(currency_symbol)
		return jsonify(
			status='success',
			endpoint='/api/currency/<currency_symbol>',
			request_method='get',
			# TODO: return wallet value at certain point in time
			currency=[currency for currency in CURRENCY if currency['currency_symbol'] == int(currency_symbol)]
		)


api_currency.add_resource(Currency, '/<currency_symbol>')


class CurrencyTime(Resource):
	"""
	Returns the candlestick with the given id
	"""

	@staticmethod
	def get(currency_symbol, timestamp):
		abort_not_found(currency_symbol)
		return jsonify(
			status='success',
			endpoint='/api/currency/<currency_symbol>/<timestamp>',
			request_method='get',
			# TODO: return wallet value at certain point in time
			currency=[currency for currency in CURRENCY if currency['symbol'] == currency_symbol and currency['closeTime'] < int(timestamp)]
		)


api_currency.add_resource(CurrencyTime, '/<currency_symbol>/<timestamp>')
