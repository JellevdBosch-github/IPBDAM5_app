from flask import Blueprint, jsonify
from flask_restful import Resource, Api, request, abort
from utils.datetime import get_current_epoch_ms
from . import module_pattern
from . import api_pattern
from database.services import pattern as service


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
			patterns=[p for p in service.browse()]
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
			count=service.count()
		)


api_pattern.add_resource(CountPattern, '/count')
