from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, abort
from utils import datetime
from . import module_wallet
from . import api_wallet
from database.services import wallet as service


# def abort_not_found(wallet_id):
# 	if not any(wallet['wallet_id'] == wallet_id for wallet in WALLET):
# 		abort(
# 			404,
# 			message={
# 				'status': 'failed',
# 				'endpoint': '/api/wallet/<wallet_id>',
# 				'request_method': 'get',
# 				'error_message': f'No wallet found matching the given id ({wallet_id})!'
# 			}
# 		)


class Wallet(Resource):
	"""
	Returns the candlestick with the given id
	"""

	@staticmethod
	def get(wallet_id):
		# abort_not_found(wallet_id)
		return jsonify(
			status='success',
			endpoint='/api/wallet/<wallet_id>',
			request_method='get',
			wallet=[wallet for wallet in service.get(wallet_id)]
		)


api_wallet.add_resource(Wallet, '/<wallet_id>')


# class WalletTime(Resource):
# 	"""
# 	Returns the candlestick with the given id
# 	"""
#
# 	@staticmethod
# 	def get(wallet_id):
# 		abort_not_found(wallet_id)
# 		return jsonify(
# 			status='success',
# 			endpoint='/api/wallet/<wallet_id>/<timestamp>',
# 			request_method='get',
# 			# TODO: return wallet value at certain point in time
# 			wallet=[wallet for wallet in WALLET if wallet['wallet_id'] == wallet_id]
# 		)
#
#
# api_wallet.add_resource(WalletTime, '/<wallet_id>/<timestamp>')
